import pygame

"""
   Programa que abra e reproduza um arquivo de audio
   mp3 direto no python

"""
pygame.init()  # inicia o módulo
pygame.mixer.music.load('ex023.mp3') #carrega o arquivo
pygame.mixer.music.play() # execulta o arquivo
pygame.event.wait()  # aguarda o termino da execução do arquivo
