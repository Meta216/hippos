# Installation

```bash
$ source ~/ros_ws/devel/setup.sh
$ cd ~/ros_ws/src
$ git clone https://github.com/Hypochondriac-Hippos/hippos.git
$ cd ~/ros_ws
$ catkin_make
```

# Use
## Launch
```bash
$ source ~/ros_ws/dev/setup.sh
$ roslaunch hippos controller.launch
```

`controller.launch` launches all competition controller nodes.

## Adding a controller
1. Add a script to `nodes`. If the script has more than one module, give it its own folder. If developed in its own repo, use `git submodule`.
2. Add a node to `launch/controller.launch`