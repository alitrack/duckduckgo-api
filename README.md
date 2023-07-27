# DuckDuckGo API

## Deploy to Vercel

[https://duckduckgo-api0.vercel.app/search?q=啊对对对是什么梗&max_results=3](https://duckduckgo-api0.vercel.app/search?q=啊对对对是什么梗&max_results=3)

使用vercel部署的本项目,免费，但是vercel免费用量用完就无了

可点下方按钮部署到自己的Vercel

[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/alitrack/duckduckgo-api)

1. 前往 [vercel.com](https://vercel.com/)
2. 点击 `Login`
![Login](https://files.catbox.moe/tct1wg.png)
3. 点击 `Continue with GitHub` 通过 GitHub 进行登录
![Continue with GitHub](https://files.catbox.moe/btd78j.jpeg)
4. 登录 GitHub 并允许访问所有存储库（如果系统这样提示）
5. Fork 这个仓库
6. 返回到你的 [Vercel dashboard](https://vercel.com/dashboard)
7. 选择 `Import Project`
![Import Project](https://files.catbox.moe/qckos0.png)
8. 选择 `Import a Git Repository`
![Import a Git Repository](https://files.catbox.moe/pqub9q.png)
9. 选择 root 并将所有内容保持不变，并且只需添加名为 PAT_1 的环境变量（如图所示），其中将包含一个个人访问令牌（PAT），你可以在[这里](https://github.com/settings/tokens/new)轻松创建（保留默认，并且只需要命名下，名字随便）
10. 点击 deploy，这就完成了，查看你的域名就可使用 API 了！
11. 注意，国内用户还得部署自己的二级域名

### Self hosting

```bash
git clone https://github.com/alitrack/duckduckgo-api.git
cd duckduckgo-api
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
uvicorn --host 0.0.0.0 --port 8000 app:app
```
