## GRPC
官网：https://github.com/grpc/grpc
文档：https://grpc.io/docs/languages/cpp/basics/


## 定义 proto 文件
```proto
service GatewayVehicleService {
    rpc GetVehicleStatus(GatewayGrpcRequest) returns (GatewayGrpcResponse) {}
    rpc UpdateVehicleStatus(GatewayGrpcRequest) returns (GatewayGrpcResponse) {}
    rpc GetVehicleRouterResult(GatewayGrpcRequest) returns (GatewayGrpcResponse) {}
    rpc GetVehicleRealRoutes(GatewayGrpcRequest) returns (GatewayGrpcResponse) {}
    rpc GetVehicleDrivingEvent(GatewayGrpcRequest) returns (GatewayGrpcResponse) {}
}

// Next id: 3
message GatewayGrpcRequest {
    optional string trace_id = 1;
    optional string access_token = 2;
    // Next id: 124.
    oneof body {
        CreateTaskForm create_task = 101;
        UpdateTaskForm update_task = 102;
        GetBizServiceTaskForm get_order_task = 103;
        GetVehicleListForm get_vehicle_status = 104;
        UpdateVehicleBizStatusForm update_vehicle_status = 105;
    }
}

// Next id: 14.
message GatewayGrpcResponse {
    optional bool ok = 1 [default = true];
    optional string msg = 2;
    optional GatewayGrpcRequest request = 3;
    optional UnifiedTaskList task_list = 4;
    optional VehicleStatusList vehicle_status_list = 5;
}

```
比如
```
service RouteGuide {
   ...
}
```
几个概念
- `stub`，就是客户端用来访问服务端的一个代理，是用来发送请求的类。
- `grpc::ClientContext`，上下文，可以放参数，控制 grpc 的一些行为。
- `grpc::Channel`，连接的网络，比如端口，host 等。

用 channel 初始化stub，用 stub 调用 grpc 接口，传入 context 参数。
