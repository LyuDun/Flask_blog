# Bilibili Leaderboard[Bilibili 热度榜]

原本的想法是每天爬Bilibili.com的全站视频，拿到每个视频的硬币、👍、收藏、评论等信息。依据不同的热度算法，展示一周内视频热度排名。为了学习Flask，此项目的结果将会在由Flask实现的我的个人博客[www.cqcqhelloworld.top](http://www.cqcqhelloworld.top/)展示。

爬虫用多进程+协程提高效率。但是实际爬取过程中,爬取速度过快容易被封。采用更换header信息，速度过快也会被禁IP。ip代理池日常维护开销大。

所以改为以当天为基准，爬取前七个自然日新投稿的视频信息。具体内容开发ing
