from lerobot.common.robot_devices.motors.configs import FeetechMotorsBusConfig
from lerobot.common.robot_devices.motors.feetech import FeetechMotorsBus

config0 = FeetechMotorsBusConfig(
        port="/dev/ttyACM0",
            motors={
                    # name: (index, model)
                    "shoulder_pan": [1, "sts3215"],
                    "shoulder_lift": [2, "sts3215"],
                    "elbow_flex": [3, "sts3215"],
                    "wrist_flex": [4, "sts3215"],
                    "wrist_roll": [5, "sts3215"],
                    "gripper": [6, "sts3215"],
                },
    )

config1 = FeetechMotorsBusConfig(
        port="/dev/ttyACM1",
            motors={
                    # name: (index, model)
                    "shoulder_pan": [1, "sts3215"],
                    "shoulder_lift": [2, "sts3215"],
                    "elbow_flex": [3, "sts3215"],
                    "wrist_flex": [4, "sts3215"],
                    "wrist_roll": [5, "sts3215"],
                    "gripper": [6, "sts3215"],
                },
    )

# 定义一个函数来处理电机操作
def handle_motors(config):
    motors_bus = FeetechMotorsBus(config)
    names = config.motors.keys()

    print(f"Connecting to motors on {config.port}...")
    motors_bus.connect()
    motors_bus.write("Torque_Enable", [128] * len(names), names)
    for name in names:
        position = motors_bus.read("Present_Position", name)
        print(f"Motor: {name}, Position: {position}")
    motors_bus.disconnect()

# 处理第一个端口
handle_motors(config0)

# 处理第二个端口
handle_motors(config1)