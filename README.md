# 图书馆管理系统后端

本项目为图书馆管理系统的后端，基于 Flask 框架开发，提供 RESTful API 用于前端与数据库的交互。适用于图书资源、用户和借阅事务的管理。

本项目为“数据库课程设计”作业。前端项目地址：[library-management-system-frontend](https://github.com/larryyan/library-management-system-frontend)

## 功能特性

- 用户认证与授权（基于 JWT）
- 图书信息管理（增删改查）
- 用户信息管理（增删改查）
- 图书借阅与归还
- 逾期图书追踪
- 数据统计与报表

## 技术栈

- Python 3.11+
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Flask-CORS
- SQLite

## 快速开始

### 环境准备

- Python 3.11 及以上
- pip

### 安装步骤

1. 克隆仓库：

   ```bash
   git clone https://github.com/larryyan/library-management-system-backend.git
   cd library-management-system-backend
   ```

2. 创建虚拟环境并激活：

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

4. 初始化数据库：

   ```bash
   flask create
   ```

5. 启动开发服务器：

   ```bash
   python app.py
   ```

   后端服务将运行在 `http://127.0.0.1:5000`。

## 主要 API 接口

- `POST   /api/login`         用户登录，获取 JWT Token
- `GET    /api/protected`     受保护接口，测试 Token
- `GET    /api/book_info`     获取所有图书详细信息
- `GET    /api/book_info/<id>`获取指定图书详细信息
- `GET    /api/book/<id>`     获取单本图书信息
- `POST   /api/book`          新增图书
- `PUT    /api/book/<id>`     更新图书
- `DELETE /api/book/<id>`     删除图书
- `GET    /api/reader/<id>`   获取用户信息
- `POST   /api/reader`        新增用户
- `PUT    /api/reader/<id>`   更新用户
- `DELETE /api/reader/<id>`   删除用户
- `POST   /api/borrow`        借书
- `POST   /api/return`        还书

详细请求与响应格式请参考前端或源码。

## 数据库结构

- `reader`    用户信息表
- `books`     图书实例表
- `book_info` 图书详细信息表
- `borrow`    借阅记录表

## 许可证

本项目采用 MIT License，详见 LICENSE 文件。
