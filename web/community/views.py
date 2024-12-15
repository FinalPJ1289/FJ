from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

# 커뮤니티
def community(request, category_id, sort_by):
    got_posts = Post.objects.all()
    categories = Category.objects.all()

    if category_id != 0:
        got_posts = got_posts.filter(category_id=category_id)

    if sort_by == 1:  # 최신순
        got_posts = got_posts.order_by('-created_at')
    elif sort_by == 2:  # 오래된순
        got_posts = got_posts.order_by('created_at')

    posts = [{'post': p} for p in got_posts]

    context = {
        'posts': posts,
        'categories': categories,
        'category_id': category_id,
    }
    return render(request, 'community.html', context)

# 게시글 쓰기
def create_post(request): # create
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid(): 
            unfinished_form = form.save(commit=False)
            unfinished_form.author = request.user
            unfinished_form.save()
            return redirect('community:community', category_id=0, sort_by=1)
    else:
        form = PostForm() 
        return render(request, 'create_post.html', {'form':form})

# 게시글 수정
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        return redirect('community:post_detail', id=post.id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('community:post_detail', id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comment_form = CommentForm(request.POST or None)  # POST 데이터가 있으면 폼에 채운다.
    
    if request.method == 'POST' and comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.linked_post = post
        comment.author = request.user  # 현재 로그인한 사용자 설정
        comment.save()
        return redirect('community:post_detail', id=post.id)
    
    comments = Comment.objects.filter(linked_post=post).order_by('created_at')
    
    context = {
        'post': post,
        'comment_form': comment_form,  # CommentForm을 컨텍스트에 추가
        'comments': comments,
    }
    
    return render(request, 'community/post_detail.html', context)
