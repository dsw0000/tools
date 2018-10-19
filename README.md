## tools
some tools

## 开发步骤

1.  编辑描述文件v2.yaml以后，根据描述文件重建UI以及项目目录
    >swagger_py_codegen --swagger-doc ./app/heweather.yaml app -p . --ui --spec

2.  实现业务逻辑
    >/onecity_v2/api/

3.  测试命令
    * 注意应该在根目录（./occapi）执行
    > python -m unittest tests.test_api

