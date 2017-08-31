print('\n'.join(list(map(lambda x: '\t'.join(x), list(map((lambda x : map((lambda y: str(y)), x)), [[x * y for y in range(1,10)] for x in range(1,10)]))))))
