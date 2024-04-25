from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Post(BaseModel):
    id: int
    title: str
    content: str


# Example data
posts = [
    Post(id=1, title="First blog", content="earth is round."),
    Post(id=2, title="Second blog", content="I am a good boy.")
]


@app.get("/posts/", response_model=List[Post])
async def get_posts():
    return posts


@app.get("/posts/{post_id}", response_model=Post)
async def get_post(post_id: int):
    for post in posts:
        if post.id == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")


@app.post("/posts/", response_model=Post)
async def create_post(post: Post):
    posts.append(post)
    return post


@app.put("/posts/{post_id}", response_model=Post)
async def update_post(post_id: int, post: Post):
    for i, p in enumerate(posts):
        if p.id == post_id:
            posts[i] = post
            return post
    raise HTTPException(status_code=404, detail="Post not found")


@app.delete("/posts/{post_id}")
async def delete_post(post_id: int):
    global posts
    posts = [p for p in posts if p.id != post_id]
    return {"message": "Post deleted"}
