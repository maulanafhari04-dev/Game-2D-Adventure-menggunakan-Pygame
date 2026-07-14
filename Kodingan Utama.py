# LIBRARY
import pygame
from sys import exit
import os
import map_project

pygame.init()
pygame.mixer.init()

# KONFIGURASI JENDELA GAME
UKURAN_UBIN = 64
JUMLAH_BARIS = 12
JUMLAH_KOLOM = 20
LEBAR_CANVAS = UKURAN_UBIN * JUMLAH_KOLOM
TINGGI_CANVAS = UKURAN_UBIN * JUMLAH_BARIS
MAP_PERMAINAN = map_project.MAP1_PERMAINAN

LEBAR_MAP = len(MAP_PERMAINAN[0]) * UKURAN_UBIN

# STATUS GAME
game_state = "INTRO"
current_map_idx = 1 
start_credits_time = 0

# VARIABEL KAMERA
kamera_x = 0

# VARIABEL PEMAIN
PEMAIN_X = LEBAR_CANVAS/2
PEMAIN_Y = TINGGI_CANVAS-2*UKURAN_UBIN
LEBAR_PEMAIN = 128
TINGGI_PEMAIN = 128

# ANIMASI DUMMY MUSUH
LEBAR_MUSUH = 96
TINGGI_MUSUH = 128

LEBAR_RUMAH = 320
TINGGI_RUMAH = 380

# KONFIGURASI FISIKA GAME
GRAFITASI = 0.6
KECEPATAN_PATROL_INTRO = 2  
KECEPATAN_MAIN = 8          
KECEPATAN_PEMAIN_Y = -14   

def load_image(folder_utama, image_name, scale=None):
    path_gambar = os.path.join(folder_utama, image_name)

    if not os.path.exists(path_gambar):
        print("TIDAK DITEMUKAN:", path_gambar)
        print("ISI FOLDER:", os.listdir(folder_utama))
        raise FileNotFoundError(path_gambar)

    image = pygame.image.load(path_gambar)

    if scale:
        image = pygame.transform.scale(image, scale)

    return image

def mainkan_bgm(nama_file):
    try:
        path_audio = os.path.join("audio_project", nama_file)
        pygame.mixer.music.load(path_audio)
        pygame.mixer.music.play(-1) 
    except:
        print(f"[AUDIO INFO] File '{nama_file}' belum tersedia.")

# MEMUAT ASET GAMBAR
gambar_background1 = load_image("images_project", "Background1.png", (LEBAR_CANVAS, TINGGI_CANVAS))
gambar_background2 = load_image("images_project", "Background2.png", (LEBAR_CANVAS, TINGGI_CANVAS))
gambar_background3 = load_image("images_project", "Background3.png", (LEBAR_CANVAS, TINGGI_CANVAS))
gambar_background4 = load_image("images_project", "Background4.png", (LEBAR_CANVAS, TINGGI_CANVAS)) 
gambar_background5 = load_image("images_project", "Background5.png", (LEBAR_CANVAS, TINGGI_CANVAS))

background_aktif = gambar_background1

gambar_rumah1 = load_image("images_project", "Rumah1.png", (LEBAR_RUMAH, TINGGI_RUMAH))
gambar_rumah2 = load_image("images_project", "Rumah2.png", (LEBAR_RUMAH, TINGGI_RUMAH))
gambar_toko = load_image("images_project", "Toko.png", (LEBAR_RUMAH, TINGGI_RUMAH))
gambar_box = load_image("images_project", "Box.png", (UKURAN_UBIN, UKURAN_UBIN))
gambar_bangku = load_image("images_project", "Bangku.png", (UKURAN_UBIN*2, UKURAN_UBIN*3))
gambar_petunjukjalan = load_image("images_project", "PetunjukJalan.png", (UKURAN_UBIN, UKURAN_UBIN*3))
gambar_lampujalan = load_image("images_project", "LampuJalan.png", (UKURAN_UBIN, UKURAN_UBIN*3))
gambar_portal = load_image("images_project", "Portal.png", (64, 128))

# MUSUH
gambar_musuh_setup = {}
gambar_musuh_jalankanan = {}
gambar_musuh_jalankiri = {}

for i in range(1,5):
    idx = i - 1
    gambar_musuh_setup[i] = [load_image("images_enemy", f"Enemy{idx}-Setup{j}.png", (LEBAR_MUSUH, TINGGI_MUSUH)) for j in range(4)]
    gambar_musuh_jalankanan[i] = [load_image("images_enemy", f"Enemy{idx}-JalanKanan{j}.png", (LEBAR_MUSUH, TINGGI_MUSUH)) for j in range(4)]
    gambar_musuh_jalankiri[i] = [load_image("images_enemy", f"Enemy{idx}-JalanKiri{j}.png", (LEBAR_MUSUH, TINGGI_MUSUH)) for j in range(4)]

# UBIN
gambar_ubinlantai1 = load_image("images_project", "UbinLantai-1.png", (UKURAN_UBIN, UKURAN_UBIN))
gambar_ubintanah1 = load_image("images_project", "UbinTanah-1.png", (UKURAN_UBIN, UKURAN_UBIN))
gambar_ubinlantai2 = load_image("images_project", "UbinLantai-2.png", (UKURAN_UBIN, UKURAN_UBIN))
gambar_ubintanah2 = load_image("images_project", "UbinTanah-2.png", (UKURAN_UBIN, UKURAN_UBIN))
gambar_ubinlantai3 = load_image("images_project", "UbinLantai-3.png", (UKURAN_UBIN, UKURAN_UBIN))
gambar_ubintanah3 = load_image("images_project", "UbinTanah-3.png", (UKURAN_UBIN, UKURAN_UBIN))
gambar_ubinlantai4 = load_image("images_project", "UbinLantai-4.png", (UKURAN_UBIN, UKURAN_UBIN))
gambar_ubintanah4 = load_image("images_project", "UbinTanah-4.png", (UKURAN_UBIN, UKURAN_UBIN))

# ANIMASI MC
gambar_MC_setup = [load_image("images_mc", f"MC-Setup{i}.png", (LEBAR_PEMAIN, TINGGI_PEMAIN)) for i in range(2)]
gambar_MC_jalankanan = [load_image("images_mc", f"MC-Jalankanan{i}.png", (LEBAR_PEMAIN, TINGGI_PEMAIN)) for i in range(4)]
gambar_MC_jalankiri = [load_image("images_mc", f"MC-JalanKiri{i}.png", (LEBAR_PEMAIN, TINGGI_PEMAIN)) for i in range(4)]
gambar_MC_lompatkanan = [load_image("images_mc", f"MC-LompatKanan{i}.png", (LEBAR_PEMAIN, TINGGI_PEMAIN)) for i in range(4)]
gambar_MC_lompatkiri = [load_image("images_mc", f"MC-LompatKiri{i}.png", (LEBAR_PEMAIN, TINGGI_PEMAIN)) for i in range(4)]
gambar_MC_serangankanan = [load_image("images_mc", f"MC-SerangKanan{i}.png", (LEBAR_PEMAIN, TINGGI_PEMAIN)) for i in range(4)]
gambar_MC_serangankiri = [load_image("images_mc", f"MC-SerangKiri{i}.png", (LEBAR_PEMAIN, TINGGI_PEMAIN)) for i in range(4)]

# ANIMASI PUTRI BARU
gambar_putri_setup = [load_image("images_putri", f"Putri-Setup{i}.png", (LEBAR_PEMAIN, TINGGI_PEMAIN)) for i in range(4)]
gambar_putri_jalankanan = [load_image("images_putri", f"Putri-JalanKanan{i}.png", (LEBAR_PEMAIN, TINGGI_PEMAIN)) for i in range(4)]
gambar_putri_jalankiri = [load_image("images_putri", f"Putri-JalanKiri{i}.png", (LEBAR_PEMAIN, TINGGI_PEMAIN)) for i in range(4)]

# Proyektil Angin
gambar_angin = []
for i in range(4):
    try:
        img = load_image("images_project", "Skill-Angin.png", (128, 128))
        gambar_angin.append(img)
    except:
        surf = pygame.Surface((64, 64), pygame.SRCALPHA)
        pygame.draw.ellipse(surf, (135, 206, 250), (0, 16, 64, 32))
        gambar_angin.append(surf)

font_judul = pygame.font.Font("Font-Judul.ttf", 46)
font_petunjuk = pygame.font.Font("Font-Petunjuk.ttf", 16)

window = pygame.display.set_mode((LEBAR_CANVAS, TINGGI_CANVAS))
pygame.display.set_caption("ADVENTURE TO BECOME A KNIGHT")
pygame.display.set_icon(gambar_MC_setup[0])
clock = pygame.time.Clock()

# ==========================================
# KELAS
# ==========================================
class DummyMusuh(pygame.Rect):
    def __init__(self, x, y, jenis=1):
        pygame.Rect.__init__(self, x, y, LEBAR_MUSUH, TINGGI_MUSUH)
        self.hp = 100
        self.jenis = jenis
        self.image = gambar_musuh_setup[self.jenis][0]
      
        self.direction = "left"
        self.status = "jalan"
        self.current_frame = 0
        self.last_update_time = pygame.time.get_ticks()
        self.animation_speed = 150  
        
        self.start_x = x
        self.patrol_range = 150     
        self.kecepatan_x = 2        
        self.tipe = "patrol"

    def terima_damage(self, jumlah_dmg):
        if self.hp > 0:
            self.hp -= jumlah_dmg
            print(f"Musuh {self.jenis} terkena serang! Sisa HP: {self.hp}")
            if self.hp <= 0:
                print(f"Musuh {self.jenis} Hancur!")
                pemain.hp = min(100, pemain.hp + 10)

    def update(self, pemain):
        if self.hp <= 0:
            return

        if self.tipe == "patrol":
            self.status = "jalan"
            if self.direction == "left":
                self.x -= self.kecepatan_x
                if self.x < self.start_x - self.patrol_range:
                    self.direction = "right"
            else:
                self.x += self.kecepatan_x
                if self.x > self.start_x + self.patrol_range:
                    self.direction = "left"

        elif self.tipe == "kejar":
            self.status = "jalan"
            if self.x < pemain.x:
                self.direction = "right"
                self.x += self.kecepatan_x
            elif self.x > pemain.x:
                self.direction = "left"
                self.x -= self.kecepatan_x

        now = pygame.time.get_ticks()
        if now - self.last_update_time > self.animation_speed:
            self.last_update_time = now
            self.current_frame = (self.current_frame + 1) % 4

        if self.status == "jalan":
            if self.direction == "left":
                self.image = gambar_musuh_jalankiri[self.jenis][self.current_frame]
            else:
                self.image = gambar_musuh_jalankanan[self.jenis][self.current_frame]
        else:
            self.image = gambar_musuh_setup[self.jenis][self.current_frame]


class ProyektilAngin(pygame.Rect):
    def __init__(self, x, y, arah):
        pygame.Rect.__init__(self, x, y, 64, 64)
        self.arah = arah
        self.kecepatan_x = 12 if arah == "right" else -12

    def update(self):
        self.x += self.kecepatan_x


class Pemain(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, PEMAIN_X, PEMAIN_Y, LEBAR_PEMAIN, TINGGI_PEMAIN)
        self.image = gambar_MC_setup[0]
        self.kecepatan_y = 0
        self.kecepatan_x = 0
        self.direction = "right"
        self.lompatan = False
        self.jalan = False
        self.serang = False
        self.current_frame = 0
        self.last_update_time = pygame.time.get_ticks()
        self.animation_speed = 300
        self.combo_count = 0
        self.last_space_time = 0
        self.hp = 100
        self.last_damage_time = 0

    def terima_damage(self, jumlah):
        now = pygame.time.get_ticks()
        if now - self.last_damage_time > 1000:
            self.hp -= jumlah
            self.last_damage_time = now
            if self.hp < 0:
                self.hp = 0
        
    def update_image(self): 
        self.animate()
        if self.serang:
            if self.direction == "left":
                self.image = gambar_MC_serangankiri[self.current_frame]
            else:
                self.image = gambar_MC_serangankanan[self.current_frame]
        elif self.lompatan: 
            if self.direction == "left": 
                self.image = gambar_MC_lompatkiri[self.current_frame]
            else: 
                self.image = gambar_MC_lompatkanan[self.current_frame]
        elif self.jalan:
            if self.direction == "right":
                self.image = gambar_MC_jalankanan[self.current_frame]
            elif self.direction == "left":
                self.image = gambar_MC_jalankiri[self.current_frame]
        else:
            frame_setup = self.current_frame % 2
            self.image = gambar_MC_setup[frame_setup]
            
    def animate(self):
        now = pygame.time.get_ticks()
        if self.serang or self.lompatan or self.jalan:
            max_frames = 4
        else:
            max_frames = 2 
      
        jeda_animasi = 80 if self.serang else self.animation_speed
        
        if now - self.last_update_time > jeda_animasi:
            self.last_update_time = now
            self.current_frame = (self.current_frame + 1) % max_frames
            
            if self.serang and self.current_frame == 0:
                self.serang = False


class Putri(pygame.Rect):
    def __init__(self, x, y):
        pygame.Rect.__init__(self, x, y, LEBAR_MUSUH, TINGGI_MUSUH)
        self.image = gambar_putri_setup[0]
        self.direction = "left"
        self.current_frame = 0
        self.last_update_time = pygame.time.get_ticks()
        self.animation_speed = 150
        self.status = "setup"

    def update(self, pemain):
        global pertemuan_selesai
        if pertemuan_selesai:
            return

        now = pygame.time.get_ticks()
        if now - self.last_update_time > self.animation_speed:
            self.last_update_time = now
            self.current_frame = (self.current_frame + 1) % 4

        if self.x > pemain.x + 80:
            self.direction = "left"
            self.x -= 3
            self.status = "jalan"
        elif self.x < pemain.x - 80:
            self.direction = "right"
            self.x += 3
            self.status = "jalan"
        else:
            self.status = "setup"

        if self.status == "jalan":
            if self.direction == "left":
                self.image = gambar_putri_jalankiri[self.current_frame]
            else:
                self.image = gambar_putri_jalankanan[self.current_frame]
        else:
            self.image = gambar_putri_setup[self.current_frame % 4]

    def draw(self, kamera_x):
        window.blit(self.image, (self.x - kamera_x, self.y))


class Rumah1(pygame.Rect):
    def __init__(self, x, y, image):
        w = image.get_width()
        h = image.get_height()
        pygame.Rect.__init__(self, x, y, w, h)
        self.image = image

class Ubin(pygame.Rect):
    def __init__(self, x, y, image):
        pygame.Rect.__init__(self, x, y, UKURAN_UBIN, UKURAN_UBIN)
        self.image = image

class Portal(pygame.Rect):
    def __init__(self, x, y, image):
        pygame.Rect.__init__(self, x, y, 64, 128)
        self.image = image

def append_ubins(map_kode, ubin):
    if map_kode < 0:
        ubin_background.append(ubin)
    else:
        ubins.append(ubin)

def buat_map():
    for kolom in range(len(MAP_PERMAINAN[0])):
        for baris in range(len(MAP_PERMAINAN)):
            kode_map = MAP_PERMAINAN[baris][kolom]
            x = kolom * UKURAN_UBIN
            y = baris * UKURAN_UBIN
            if kode_map == 0:
                continue
            elif abs(kode_map) == 1:
                append_ubins(kode_map, Ubin(x, y, gambar_ubinlantai1))
            elif abs(kode_map) == 2:
                append_ubins(kode_map, Ubin(x, y, gambar_ubintanah1))
            elif abs(kode_map) == 3:
                append_ubins(kode_map, Ubin(x, y, gambar_ubinlantai2))
            elif abs(kode_map) == 4:
                append_ubins(kode_map, Ubin(x, y, gambar_ubintanah2))
            elif abs(kode_map) == 5:
                append_ubins(kode_map, Ubin(x, y, gambar_ubinlantai3))
            elif abs(kode_map) == 6:
                append_ubins(kode_map, Ubin(x, y, gambar_ubintanah3))
            elif abs(kode_map) == 7:
                append_ubins(kode_map, Ubin(x, y, gambar_ubinlantai4))
            elif abs(kode_map) == 8:
                append_ubins(kode_map, Ubin(x, y, gambar_ubintanah4))
            elif abs(kode_map) == 11:
                ubin_background.append(Ubin(x, y, gambar_box))
            elif abs(kode_map) == 12:
                posisi_y_pas = y + UKURAN_UBIN - 380
                rumah1.append(Rumah1(x, posisi_y_pas, gambar_rumah1))
            elif abs(kode_map) == 13:
                posisi_y_pas = y + UKURAN_UBIN - 380
                rumah1.append(Rumah1(x, posisi_y_pas, gambar_rumah2))
            elif abs(kode_map) == 14:
                posisi_y_pas = y + UKURAN_UBIN - 380
                rumah1.append(Rumah1(x, posisi_y_pas, gambar_toko))
            elif abs(kode_map) == 15:
                posisi_y_pas = y + UKURAN_UBIN - UKURAN_UBIN*3
                rumah1.append(Rumah1(x, posisi_y_pas, gambar_bangku))
            elif abs(kode_map) == 16:
                posisi_y_pas = y + UKURAN_UBIN - 32
                rumah1.append(Rumah1(x, posisi_y_pas, gambar_petunjukjalan))
            elif abs(kode_map) == 17:
                posisi_y_pas = y + UKURAN_UBIN - UKURAN_UBIN*3
                rumah1.append(Rumah1(x, posisi_y_pas, gambar_lampujalan))
            elif abs(kode_map) == 18:
                posisi_y_pas = y + UKURAN_UBIN - 128
                portals.append(Portal(x, posisi_y_pas, gambar_portal))
            elif abs(kode_map) in [20, 21, 22, 23]:
                jenis_musuh = abs(kode_map) - 19
                posisi_y_pas = y + UKURAN_UBIN - TINGGI_MUSUH
                musuh_baru = DummyMusuh(x, posisi_y_pas, jenis=jenis_musuh)
                musuh_baru.tipe = "kejar"
                list_musuh.append(musuh_baru)

def pindah_map(peta_baru, background_baru, map_idx):
    global MAP_PERMAINAN, LEBAR_MAP, background_aktif, current_map_idx, putri, pertemuan_selesai
    MAP_PERMAINAN = peta_baru
    background_aktif = background_baru
    LEBAR_MAP = len(MAP_PERMAINAN[0]) * UKURAN_UBIN
    
    ubins.clear()
    ubin_background.clear()
    rumah1.clear()
    portals.clear()
    list_angin.clear()
    list_musuh.clear() 
 
    buat_map()
    
    if peta_baru == map_project.MAP1_PERMAINAN:
        current_map_idx = 1
        pemain.hp = 100
        mainkan_bgm("bgm_intro.mp3")
    elif peta_baru == map_project.MAP2_PERMAINAN:
        current_map_idx = 2
        musuh_patrol = DummyMusuh(1300, TINGGI_CANVAS - 2 * UKURAN_UBIN - TINGGI_MUSUH, jenis=1)
        musuh_patrol.tipe = "patrol"
        list_musuh.append(musuh_patrol)
        mainkan_bgm("bgm_map2.mp3")
    elif peta_baru == map_project.MAP3_PERMAINAN:
        current_map_idx = 3
        mainkan_bgm("bgm_map3.mp3")
    elif peta_baru == map_project.MAP4_PERMAINAN:
        current_map_idx = 4
        mainkan_bgm("bgm_map4.mp3")
    elif peta_baru == map_project.MAP5_PERMAINAN:
        current_map_idx = 5
        mainkan_bgm("bgm_map5.mp3")
        putri = Putri(LEBAR_MAP - 500, TINGGI_CANVAS - 2*UKURAN_UBIN - TINGGI_MUSUH)
        pertemuan_selesai = False
    else:
        current_map_idx = map_idx
        
    pemain.x = 100 
    pemain.y = TINGGI_CANVAS - 2 * UKURAN_UBIN
    pemain.kecepatan_y = 0

def move():
    global kamera_x, game_state

    if game_state == "CREDITS":
        return

    if game_state == "INTRO":
        pemain.jalan = True
        if pemain.direction == "right":
            pemain.kecepatan_x = KECEPATAN_PATROL_INTRO 
            if pemain.x >= LEBAR_CANVAS - LEBAR_PEMAIN - 64:
                pemain.direction = "left"
        else:
            pemain.kecepatan_x = -KECEPATAN_PATROL_INTRO
            if pemain.x <= 64:
                pemain.direction = "right"
        pemain.x += pemain.kecepatan_x
        kamera_x = 0

    elif game_state == "TRANSITION":
        pemain.jalan = True
        target_tengah_x = (LEBAR_CANVAS / 2) - (pemain.width / 2)
        if pemain.x < target_tengah_x:
            pemain.direction = "right"
            pemain.kecepatan_x = KECEPATAN_MAIN 
            pemain.x += pemain.kecepatan_x
            if pemain.x >= target_tengah_x:
                pemain.x = target_tengah_x
                game_state = "PLAYING"
        elif pemain.x > target_tengah_x:
            pemain.direction = "left"
            pemain.kecepatan_x = -KECEPATAN_MAIN
            pemain.x += pemain.kecepatan_x
            if pemain.x <= target_tengah_x:
                pemain.x = target_tengah_x
                game_state = "PLAYING"
        kamera_x = 0

    elif game_state == "PLAYING":
        pemain.x += pemain.kecepatan_x 
        if pemain.x < 0: 
            pemain.x = 0 
        elif pemain.x + pemain.width > LEBAR_MAP: 
            pemain.x = LEBAR_MAP - pemain.width 
        
        for ubin in ubins:
            if pemain.colliderect(ubin):
                if pemain.kecepatan_x > 0:   
                    pemain.right = ubin.left 
                elif pemain.kecepatan_x < 0: 
                    pemain.left = ubin.right 

        for portal in portals:
            if pemain.colliderect(portal):
                if current_map_idx in [3, 4]:
                    if any(m.hp > 0 for m in list_musuh):
                        return
                pemain.jalan = False
                pemain.kecepatan_x = 0
                game_state = "PROMPT" 

        kamera_x = pemain.x - (LEBAR_CANVAS / 2) + (pemain.width / 2)
        kamera_x = max(0, min(kamera_x, LEBAR_MAP - LEBAR_CANVAS))

    if game_state not in ["PROMPT", "GAMEOVER", "MAP5_DIALOG", "MAP5_VICTORY"]: 
        pemain.kecepatan_y += GRAFITASI 
        pemain.y += pemain.kecepatan_y 
        
        for ubin in ubins:
            if pemain.colliderect(ubin):
                if pemain.kecepatan_y > 0:    
                    pemain.bottom = ubin.top  
                    pemain.kecepatan_y = 0    
                    pemain.lompatan = False   
                elif pemain.kecepatan_y < 0:  
                    pemain.top = ubin.bottom 
                    pemain.kecepatan_y = 0    
                    
        if pemain.y > TINGGI_CANVAS or pemain.hp <= 0:
            pygame.mixer.music.stop()
            game_state = "GAMEOVER"

def draw():
    if game_state == "CREDITS":
        window.fill((10, 10, 25)) 
        
        now = pygame.time.get_ticks()
        waktu_berjalan = now - start_credits_time
        
        pos_y_awal = TINGGI_CANVAS
        kecepatan_scroll = 0.06 
        
        teks_kredit = [
            "TERIMA KASIH TELAH BERMAIN!",
            "",
            "ADVENTURE TO BECOME A KNIGHT",
            "",
            "--- KREDIT EDITOR ---",
            "Lead Programmer: [MAULANA FHADEL AZHARI]",
            "Graphic Designer: [FIKHRI DZAKKI"
                              "TAUFIQ QURAHMAN]",
            "Level Designer: [WANDA IRAWATI"
                        "MAULANA FHADEL AZHARI]",
            "Audio & Music Composer: [FIKHRI DZAKKI"
                                    "TAUFIQ QURAHMAN]",
            "",
            "--- DIDUKUNG OLEH ---",
            "Python & Pygame Community",
            "",
            "Selamat! Anda berhasil memenangkan Sayembara Putri!",
            "",
            "Tekan [ENTER] untuk kembali ke Menu Utama"
        ]
        
        for i, baris in enumerate(teks_kredit):
            y_pos = pos_y_awal - (waktu_berjalan * kecepatan_scroll) + (i * 42)
            
            if -50 < y_pos < TINGGI_CANVAS + 50:
                if i == 0 or "Tekan [ENTER]" in baris or "Selamat!" in baris:
                    warna_teks = (255, 215, 0) 
                elif "---" in baris:
                    warna_teks = (0, 255, 120) 
                else:
                    warna_teks = (255, 255, 255) 
                    
                surf_teks = font_petunjuk.render(baris, True, warna_teks)
                rect_teks = surf_teks.get_rect(center=(LEBAR_CANVAS // 2, y_pos))
                window.blit(surf_teks, rect_teks)
        return

    window.blit(background_aktif, (0, 0)) 

    for rumah in rumah1:
        if rumah.x - kamera_x > -340 and rumah.x - kamera_x < LEBAR_CANVAS:
            window.blit(rumah.image, (rumah.x - kamera_x, rumah.y))

    for portal in portals:
        if portal.x - kamera_x > -64 and portal.x - kamera_x < LEBAR_CANVAS:
            window.blit(portal.image, (portal.x - kamera_x, portal.y))
    
    for ubin in ubin_background:
        if ubin.x - kamera_x > -UKURAN_UBIN and ubin.x - kamera_x < LEBAR_CANVAS:
            window.blit(ubin.image, (ubin.x - kamera_x, ubin.y))

    for ubin in ubins:
        if ubin.x - kamera_x > -UKURAN_UBIN and ubin.x - kamera_x < LEBAR_CANVAS:
            window.blit(ubin.image, (ubin.x - kamera_x, ubin.y))

    for musuh in list_musuh:
        if musuh.hp > 0:
            window.blit(musuh.image, (musuh.x - kamera_x, musuh.y))
            teks_hp = font_petunjuk.render(f"E{musuh.jenis} HP: {musuh.hp}/100", True, (255, 255, 255))
            window.blit(teks_hp, (musuh.x - kamera_x, musuh.y - 25))

    for angin in list_angin:
        frame_aktif = (pygame.time.get_ticks() // 100) % 4
        window.blit(gambar_angin[frame_aktif], (angin.x - kamera_x, angin.y))

    if current_map_idx == 5 and putri:
        putri.draw(kamera_x)

    pemain.update_image() 
    window.blit(pemain.image, (pemain.x - kamera_x, pemain.y)) 

    if game_state == "PLAYING":
        pygame.draw.rect(window, (50, 50, 50), (20, 20, 200, 25))
        lebar_hp = int(200 * (max(0, pemain.hp) / 100))
        warna_hp_bar = (0, 255, 100) if pemain.hp > 30 else (255, 50, 50)
        pygame.draw.rect(window, warna_hp_bar, (20, 20, lebar_hp, 25))
        pygame.draw.rect(window, (255, 255, 255), (20, 20, 200, 25), 2)
        teks_hp_pemain = font_petunjuk.render(f"HP: {pemain.hp}/100", True, (255, 255, 255))
        window.blit(teks_hp_pemain, (30, 24))

    if game_state == "PLAYING" and current_map_idx == 2:
        if pemain.x < 500:
            string_teks = "Tekan [A] atau [D] / Tombol Panah untuk jalan"
        elif 500 <= pemain.x < 950:
            string_teks = "Tekan [W] atau Panah Atas untuk melompat rintangan"
        elif 950 <= pemain.x < 1250:
            string_teks = "Dekati Target! Tekan [SPASI] untuk menyerang (20 DMG)"
        else:
            string_teks = "Coba KOMBO: Jalan Kanan/Kiri + Tekan [SPASI] 2x untuk Lempar Angin (30 DMG)!"

        teks_tutorial = font_petunjuk.render(string_teks, True, (0, 255, 100))
        lebar_t, tinggi_t = teks_tutorial.get_size()
        
        box_t_x = (pemain.x - kamera_x) + (pemain.width // 2) - (lebar_t // 2)
        box_t_y = pemain.y - 45
        
        surf_bg = pygame.Surface((lebar_t + 16, tinggi_t + 8))
        surf_bg.fill((0, 0, 0))
        surf_bg.set_alpha(180)
        window.blit(surf_bg, (box_t_x - 8, box_t_y - 4))
        window.blit(teks_tutorial, (box_t_x, box_t_y))

    if game_state == "INTRO":
        teks_judul = font_judul.render("ADVENTURE TO BECOME A KNIGHT", True, (255, 0, 0))
        rect_judul = teks_judul.get_rect(center=(LEBAR_CANVAS // 2, TINGGI_CANVAS // 3))
        rect_bayangan = rect_judul.copy()
        rect_bayangan.x += 3
        rect_bayangan.y += 3
        window.blit(font_judul.render("ADVENTURE TO BECOME A KNIGHT", True, (0, 0, 0)), rect_bayangan)
        window.blit(teks_judul, rect_judul)
        
        if (pygame.time.get_ticks() // 500) % 2 == 0:
            teks_info = font_petunjuk.render("PRESS ENTER TO START GAME", True, (0, 0, 0))
            rect_info = teks_info.get_rect(center=(LEBAR_CANVAS // 2, TINGGI_CANVAS // 2 + 30))
            window.blit(teks_info, rect_info)

    elif game_state == "PROMPT":
        lebar_box, tinggi_box = 550, 150
        box_x = (LEBAR_CANVAS - lebar_box) // 2
        box_y = (TINGGI_CANVAS - tinggi_box) // 2
        overlay = pygame.Surface((lebar_box, tinggi_box))
        overlay.set_alpha(220)
        overlay.fill((0, 0, 0))
        window.blit(overlay, (box_x, box_y))
        pygame.draw.rect(window, (255, 255, 255), (box_x, box_y, lebar_box, tinggi_box), 3)
        
        if current_map_idx == 1:
            string_tanya = "Mulai memainkan Sayembara sang putri?"
        elif current_map_idx == 5:
            string_tanya = "Selesaikan Sayembara sang putri dan kembali?"
        else:
            string_tanya = f"Lanjut ke area Map {current_map_idx + 1}?"

        teks_tanya = font_petunjuk.render(string_tanya, True, (255, 255, 255))
        rect_tanya = teks_tanya.get_rect(center=(LEBAR_CANVAS // 2, box_y + 45))
        window.blit(teks_tanya, rect_tanya)
        
        teks_opsi = font_petunjuk.render("[Y] YES (Mulai)    /   [N] NO (Stay)", True, (255, 215, 0))
        rect_opsi = teks_opsi.get_rect(center=(LEBAR_CANVAS // 2, box_y + 105))
        window.blit(teks_opsi, rect_opsi)

    elif game_state == "GAMEOVER":
        window.fill((30, 5, 5)) 
        teks_go = font_judul.render("GAME OVER", True, (240, 30, 30))
        rect_go = teks_go.get_rect(center=(LEBAR_CANVAS // 2, TINGGI_CANVAS // 3))
        window.blit(teks_go, rect_go)

        teks_hint = font_petunjuk.render("PRESS ENTER TO RETURN TO MAIN MENU", True, (255, 255, 255))
        rect_hint = teks_hint.get_rect(center=(LEBAR_CANVAS // 2, TINGGI_CANVAS // 2 + 40))
        window.blit(teks_hint, rect_hint)

    elif game_state == "MAP5_DIALOG":
        box_width = 720
        box_height = 200
        box_x = (LEBAR_CANVAS - box_width) // 2
        box_y = TINGGI_CANVAS // 2 - 90
        
        dialog_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        dialog_surface.fill((255, 255, 255, 235))
        window.blit(dialog_surface, (box_x, box_y))
        
        pygame.draw.rect(window, (0, 0, 0), (box_x, box_y, box_width, box_height), 6)
        pygame.draw.rect(window, (255, 215, 0), (box_x, box_y, box_width, box_height), 4)

        dialog_texts = [
            "Kamu akhirnya datang Pahlawanku!",
            "Sayembara ini dimenangkan oleh mu.",
            "Terima Kasih... Sekarang ikut aku ya."
        ]
        
        for i, txt in enumerate(dialog_texts):
            text_surf = font_petunjuk.render(txt, True, (0, 0, 0))
            text_rect = text_surf.get_rect(center=(LEBAR_CANVAS//2, box_y + 55 + i*45))
            window.blit(text_surf, text_rect)

        continue_text = font_petunjuk.render("Tekan ENTER untuk melanjutkan", True, (0, 80, 0))
        continue_rect = continue_text.get_rect(center=(LEBAR_CANVAS//2, box_y + box_height - 15))
        window.blit(continue_text, continue_rect)

# Inisialisasi
pemain = Pemain()
pemain.x = 100 
putri = None
pertemuan_selesai = False

portals = []
rumah1 = []
ubins = []
ubin_background = []
list_angin = [] 
list_musuh = []

buat_map()
mainkan_bgm("bgm_intro.mp3") 

# GAME LOOP UTAMA
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
             
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                if game_state == "INTRO":
                    target_tengah_x = (LEBAR_CANVAS / 2) - (pemain.width / 2)
                    jarak_ke_target = abs(pemain.x - target_tengah_x)
                    if jarak_ke_target > 100:
                        pemain.x = target_tengah_x  
                        game_state = "PLAYING"      
                    else:
                        game_state = "TRANSITION"   
                elif game_state == "GAMEOVER":
                    game_state = "INTRO"
                    pindah_map(map_project.MAP1_PERMAINAN, gambar_background1, 1) 
                elif game_state == "CREDITS":
                    game_state = "INTRO"
                    pindah_map(map_project.MAP1_PERMAINAN, gambar_background1, 1)
                elif game_state == "MAP5_DIALOG":
                    game_state = "MAP5_VICTORY"
                elif game_state == "MAP5_VICTORY":
                    game_state = "CREDITS"
                    start_credits_time = pygame.time.get_ticks()
                    mainkan_bgm("bgm_credits.mp3")

            elif game_state == "PLAYING" and event.key == pygame.K_SPACE:
                now = pygame.time.get_ticks()
                keys = pygame.key.get_pressed()
                if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) or (keys[pygame.K_LEFT] or keys[pygame.K_a]):
                    if now - pemain.last_space_time < 450: 
                        pemain.combo_count += 1
                    else:
                        pemain.combo_count = 1
                else:
                    pemain.combo_count = 0 
                pemain.last_space_time = now

                if pemain.combo_count == 2:
                    pemain.serang = True
                    pemain.current_frame = 0
                    spawn_x = pemain.right if pemain.direction == "right" else pemain.left - 64
                    list_angin.append(ProyektilAngin(spawn_x, pemain.centery - 32, pemain.direction))
                    print("KOMBO AKTIF! Melempar Angin (30 DMG)!")
                    pemain.combo_count = 0 
                else:
                    if not pemain.serang:
                        pemain.serang = True
                        pemain.current_frame = 0
                        print("MC Menyerang! Memberikan 20 DMG!")
                        for musuh in list_musuh:
                            if musuh.hp > 0 and pemain.colliderect(musuh):
                                musuh.terima_damage(20)

            elif game_state == "PROMPT":
                if event.key == pygame.K_y:
                    if current_map_idx == 1:
                        pindah_map(map_project.MAP2_PERMAINAN, gambar_background2, 2)
                        game_state = "PLAYING"
                    elif current_map_idx == 2:
                        pindah_map(map_project.MAP3_PERMAINAN, gambar_background3, 3)
                        game_state = "PLAYING"
                    elif current_map_idx == 3:
                        pindah_map(map_project.MAP4_PERMAINAN, gambar_background4, 4)
                        game_state = "PLAYING"
                    elif current_map_idx == 4:
                        pindah_map(map_project.MAP5_PERMAINAN, gambar_background5, 5)
                        game_state = "PLAYING"
                    elif current_map_idx == 5:
                        game_state = "MAP5_DIALOG"
                elif event.key == pygame.K_n:
                    game_state = "PLAYING"
                    if pemain.direction == "right":
                        pemain.x -= 60
                    else:
                        pemain.x += 60

    if game_state == "CREDITS":
        now = pygame.time.get_ticks()
        if now - start_credits_time > 12000: 
            game_state = "INTRO"
            pindah_map(map_project.MAP1_PERMAINAN, gambar_background1, 1)

    if game_state == "PLAYING":
        for musuh in list_musuh:
            musuh.update(pemain)
            if musuh.hp > 0 and pemain.colliderect(musuh):
                pemain.terima_damage(10)

        for angin in list_angin[:]:
            angin.update()
            tertabrak = False
            for musuh in list_musuh:
                if musuh.hp > 0 and angin.colliderect(musuh):
                    musuh.terima_damage(30) 
                    list_angin.remove(angin)
                    tertabrak = True
                    break 
            if not tertabrak and (angin.x < 0 or angin.x > LEBAR_MAP):
                list_angin.remove(angin)

        if current_map_idx == 5 and putri and not pertemuan_selesai:
            putri.update(pemain)
            if abs(pemain.x - putri.x) < 150:
                pertemuan_selesai = True
                game_state = "MAP5_DIALOG"

        keys = pygame.key.get_pressed() 
        pemain.kecepatan_x = 0
        pemain.jalan = False

        if keys[pygame.K_LEFT] or keys[pygame.K_a]: 
            pemain.kecepatan_x = -KECEPATAN_MAIN
            pemain.direction = "left" 
            if not pemain.serang: 
                pemain.jalan = True
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            pemain.kecepatan_x = KECEPATAN_MAIN
            pemain.direction = "right"
            if not pemain.serang:
                pemain.jalan = True

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and not pemain.lompatan: 
            pemain.kecepatan_y = KECEPATAN_PEMAIN_Y 
            pemain.lompatan = True 

    move()
    draw()
    pygame.display.update() 
    clock.tick(60)
