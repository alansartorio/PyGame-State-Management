from abc import abstractmethod
import pygame
from pygame import Surface
from pygame.event import Event
from pygame.locals import *
from pygame.time import Clock
from typing import List


class GameState:
	@abstractmethod
	def enter(self):
		pass
	@abstractmethod
	def leave(self):
		pass

	@abstractmethod
	def load(self):
		pass
	@abstractmethod
	def dispose(self):
		pass

	@abstractmethod
	def update(self, dt: float, events: List[Event]):
		pass
	@abstractmethod
	def draw(self, surface: Surface):
		pass




class Game:
	def __init__(self, width = 640, height = 480, audioBuffer = 8):
		pygame.mixer.pre_init(buffer=audioBuffer)
		pygame.init()
		self.width = width
		self.height = height
		self.states: List[GameState] = []
	
	def pushState(self, state: GameState):
		if len(self.states) > 0:
			self.states[-1].leave()
		self.states.append(state)
		state.load()
		state.enter()
	
	def popState(self):
		popped = self.states.pop()
		popped.leave()
		popped.dispose()

		if len(self.states) > 0:
			self.states[-1].enter()
		else:
			self.running = False
	
	def popAndPushState(self, state: GameState):
		popped = self.states.pop()
		popped.leave()
		popped.dispose()

		self.states.append(state)
		state.load()
		state.enter()
	
	def reloadState(self):
		state = self.states[-1]
		state.dispose()
		state.load()

	def quit(self):
		self.states[-1].leave()
		for state in self.states:
			state.dispose()
		self.states.clear()
		self.running = False

	def run(self, framerate: int = 0):
		self.running = True
		clock = Clock()
		surface = pygame.display.set_mode((self.width, self.height))
		while self.running:
			dt = clock.tick(framerate) / 1000

			currentState = self.states[-1]

			events = pygame.event.get()
			for event in events:
				if event.type == QUIT:
					self.running = False
			if not self.running:continue
			currentState.update(dt, events)
			if not self.running:continue
			surface.fill((0, 0, 0))
			currentState.draw(surface)

			pygame.display.flip()
