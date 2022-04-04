class button:
    def __init__(self, pos, text_input, font, base_color, hovering_color):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.rect = self.text.get_rect(center =(self.x_pos,self.y_pos))
        
        
    def check_na_stlacenie(self, pozicia):
        if pozicia[0] in range(self.rect.left, self.rect.right) and pozicia[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def zmenenie_farby(self, pozicia):
        if pozicia[0] in range(self.rect.left, self.rect.right) and pozicia[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def aktualizuj(self,okno):
        okno.blit(self.text,self.rect)