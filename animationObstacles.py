class Kong(pygame.sprite.Sprite):
    def update(self):
            #check if the player has picked up the box
            if pygame.sprite.collide_rect(self, player):
                #check what kind of box it was
                if self.item_type == 'Health':
                    player.health += 25
                    if player.health > player.max_health:
                        player.health = player.max_health
                elif self.item_type == 'Ammo':
                    player.ammo += 15
                elif self.item_type == 'Grenade':
                    player.grenades += 3
                #delete the item box
                self.kill() 

    #bullet collision
            if pygame.sprite.spritecollide(player, bullet_group, False):
                if player.alive:
                    player.health -= 5
                    self.kill()
            for enemy in enemy_group:
                if pygame.sprite.spritecollide(enemy, bullet_group, False):
                    if enemy.alive:
                        enemy.health -= 25
                        self.kill()


                        #check collision with floor
            if self.rect.bottom + dy > 300:
                dy = 300 - self.rect.bottom
                self.speed = 0

            #check collision with walls
            if self.rect.left + dx < 0 or self.rect.right + dx > SCREEN_WIDTH:
                self.direction *= -1
                dx = self.direction * self.speed


