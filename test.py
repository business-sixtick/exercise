import test_module
tm = test_module.c_test()
tm.run()
# 아 노트에서는 안되는데 py에서는 모듈 else 구문이 타네

import inspect    #모듈 위치를 알아내는 모듈
print(inspect.getfile(test_module)) # 예시



