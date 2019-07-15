# Django-on-Docker
> docker + django + nginx + postgres + gunicorn demo

## Development setup

```sh
git clone git@github.com:XiangHuang1992/django-on-docker.git # 下载到本地

# dev
docker-compose up -d --build 


# prod(添加了nginx和gunicorn)
docker-compose -f docker-compose.prod.yml  up -d --build # 生产环境，添加了nginx和gunicorn

docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput # django migrate

docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear # staticfile and mediafiles collect
```