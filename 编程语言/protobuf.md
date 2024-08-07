### protobuf 常用函数

```python
from google.protobuf import json_format

# 1. 把 message 转成 dict；
json_format.MessageToDict(
    message,
    including_default_value_fields=False,   # 这个参数默认会过滤没有设置的字段
    preserving_proto_field_name=False,      # 这个参数默认会改变 field_name 为驼峰命名
    use_integers_for_enums=False,
    descriptor_pool=None,
    float_precision=None
)

# 2. 把 dict 转成 message
json_format.ParseDict(js_dict, message, ignore_unknown_fields=False)

# 3. 把 message 转成 json
json_format.MessageToJson(
    message,
    including_default_value_fields=False,
    preserving_proto_field_name=False,
    indent=2,
    sort_keys=False,
    use_integers_for_enums=False,
)

# 4. 把 json 转成 message
json_format.Parse(text, message, ignore_unknown_fields=False)

```

