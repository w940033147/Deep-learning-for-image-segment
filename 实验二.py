#!/usr/bin/env python




import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderer,
    vtkRenderWindowInteractor

)


def main(argv):
    #
    # 接下来，我们创建一个 vtkNamedColors 的实例，我们将使用此选项为对象和背景选择颜色。
    #
    colors = vtkNamedColors()
    bkg = map(lambda x: x / 255.0, [26, 51, 102, 255])
    colors.SetColor("BkgColor", *bkg)
    #
    # 现在，我们创建一个 vtkConeSource 的实例并设置其一些属性。
    # vtkConeSource“cone”的实例是可视化管道的一部分（它是一个源进程对象），
    # 它生成其他过滤器可以处理的数据（输出类型为vtkPolyData）。
    #
    cone = vtkConeSource()
    cone.SetHeight(3.0)
    cone.SetRadius(1.0)
    cone.SetResolution(10)

    #
    # 在此示例中，我们使用映射器进程对象终止管道。
    #  （中间筛选器（如 vtkShrinkPolyData）可以插入到源和映射器之间。
    #  我们创建一个 vtkPolyDataMapper 实例，
    #  以将多边形数据映射到图形基元中。
    #  我们将锥体源的输出连接到此映射器的输入。
    #
    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())

    #
    # 创建一个执行组件来表示圆锥体。执行组件协调映射器的图形基元的呈现。
    # 参与者还通过 vtkProperty 实例引用属性，并包括内部转换矩阵。
    # 我们将这个演员的映射器设置为我们上面创建的锥形映射器。
    #
    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.GetProperty().SetColor(colors.GetColor3d('MistyRose'))

    #
    #创建渲染器并向其分配角色。渲染器就像一个视口。
    # 它是屏幕上窗口的一部分或全部，
    # 负责绘制它所拥有的演员。
    # 我们还在此处设置了背景色。
    #
    ren1 = vtkRenderer()
    ren1.AddActor(coneActor)
    ren1.SetBackground(colors.GetColor3d('MidnightBlue'))

    # 最后，我们创建渲染窗口，该窗口将显示在屏幕上。
    # 我们使用 AddRenderer 将渲染器放入渲染窗口中。我们还
    # 将大小设置为 300 x 300 像素。
    #
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    renWin.SetSize(300, 300)
    renWin.SetWindowName('Tutorial_Step1')

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    iren.Initialize()
    #
    # 现在，我们循环超过 360 度，每次都渲染锥体。
    #
    for i in range(0, 360):
        # 渲染图像
        renWin.Render()
        # 将活动相机旋转一度。
        ren1.GetActiveCamera().Azimuth(1)
    iren.Start()


if __name__ == '__main__':
    import sys

    main(sys.argv)