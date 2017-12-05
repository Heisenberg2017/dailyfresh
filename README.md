# dailyfresh

1. 主页
    1.1 商品分类展示，点击可跳转至商品详情页面
    1.2 提供登陆/注册入口，登陆后显示用户名，点击可跳转至个人中心
    1.3 按商品上架时间和点击量进行排序展示
    1.4 提供搜索入口
    1.5 退出登录功能

2. 注册
    2.1 异步检验用户名是否已存在
    2.2 注册信息提交前检验用户输入是否正确
    2.3 保存用户名
    2.4 注册成功跳转至主页

3. 登陆
    3.1 用用户名与密码登陆
    3.2 错误时有相应提示

4. 商品列表页
    4.1 提供最新本类最新商品信息2条
    4.2 可根据商品录入时间，价格，点击率进行升序或降序排列
    4.3 商品分类展示

5. 商品详情页
    5.1 展示单个商品信息
    5.2 django admin商品详情录入选用tinymce作为富文本编辑器

6. 个人中心页
    6.1 展示用户个人信息
    6.2 展示用户最近浏览的5条商品信息
    6.3 展示用户订单

7. 购物页
    7.1 展示用户添加加入购物车商品
    7.2 提供添加,修改,删除功能

8. 订单页
    8.1 付款方式，商品信息
    8.2 提交订单

9. 个人中心订单页
    9.1 订单信息分页展示
    
10. 搜索
    10.1 提供全文检索功能(haystack+whoosh+jieba)
