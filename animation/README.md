# 启动动画源码

`index.html` 是 1920×1080、30 fps、14.4 秒的 HyperFrames 画面。`assets/lu-mingfei-cyber.png` 以用户提供的竖版路明非插画为参考，用内置图像编辑工具扩展成横版红黑电子风背景；并非直接拉伸原图。生成提示词要求保留黑发、灰色兜帽、深色连帽衫、神态，将人物放在左侧，右侧留出标题空间，不加入文字、标志或其他人物。人物背景的权利说明见 `../media/MEDIA_NOTICE.md`。

使用 `python generate_audio.py` 可重建合成音轨；使用 `npx hyperframes check` 检查画面，再使用 `npx hyperframes render --quality delivery --output ../media/startup.mp4` 渲染。CLI 版本固定在 `package.json`。

视频结尾的矩形窗口从 12.45 秒开始放大，13.95 秒填满画面。若改动 `#portal` 的位置、尺寸、缓动或时间，必须同步重新标定 `../config/launcher.example.json` 的 `ScreenFrames`、`TransitionStart` 和 `TransitionEnd`。
