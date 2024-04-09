import pygame

# 初始化Pygame
pygame.init()

# 创建游戏窗口
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame测试")

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 绘制背景
    window.fill((255, 255, 255))

    # 刷新窗口
    pygame.display.update()

# 退出游戏
pygame.quit()