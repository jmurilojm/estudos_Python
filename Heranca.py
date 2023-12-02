class Eletronico():
	
	def __init__(self):
		self.ligado = False
	
	def ligar(self):
		self.ligado = True
		
	def desligar(self):
		self.ligado = False
		
	def status_ligado(self):
		if self.ligado == True:
			return 'Ligado'
		else:
			return 'Desligado'
		
class Tv(Eletronico):
	
	def __init__(self):
		Eletronico.__init__(self)
		self.volume = 0
		
	def aumentar_volume(self):
		if self.ligado == True:
			self.volume += 1
		else:
			print('TV está desligada!')
		
	def diminuir_volume(self):
		if self.volume > 0:
			self.volume -= 1
	
	def status_volume(self):
		return self.volume
	
class iphone(Eletronico):
	
	def __init__(self):
		Eletronico.__init__(self)
		self.tocando_musica = False
		
	def tocar_musica(self):
		self.tocando_musica = True
		
	def parar_musica(self):
		self.tocando_musica = False
		
	def status_tocando(self):
		return self.tocando_musica
		
#================================================

tv1 = Tv()

tv1.aumentar_volume()
print(tv1.status_ligado())
print(tv1.status_volume())


tv1.ligar()
tv1.aumentar_volume()
print(tv1.status_ligado())
print(tv1.status_volume())
