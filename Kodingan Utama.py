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

# VARIABEL KAMERA
kamera_x = 0

# VARIABEL PEMAIN
PEMAIN_X = LEBAR_CANVAS/2
PEMAIN_Y = TINGGI_CANVAS-2*UKURAN_UBIN
LEBAR_PEMAIN = 128
TINGGI_PEMAIN = 128

# VARIABEL RUMAH1 (Ukuran dasar gedung)
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

# ==========================================
# MEMUAT ASET GAMBAR & FONT (UKURAN FIX PAS)
# ==========================================
gambar_background1 = load_image("images_project", "Background1.png", (LEBAR_CANVAS, TINGGI_CANVAS))
gambar_background2 = load_image("images_project", "Background2.png", (LEBAR_CANVAS, TINGGI_CANVAS))
gambar_background3 = load_image("images_project", "Background3.png", (LEBAR_CANVAS, TINGGI_CANVAS))
gambar_background4 = load_image("images_project", "Background4.png", (LEBAR_CANVAS, TINGGI_CANVAS)) 
gambar_background5 = load_image("images_project", "Background5.png", (LEBAR_CANVAS, TINGGI_CANVAS))

background_aktif = gambar_background1

# Properti & Bangunan (Sesuai Request Ukuran Pas)
gambar_rumah1 = load_image("images_project", "Rumah1.png", (LEBAR_RUMAH, TINGGI_RUMAH))
gambar_rumah2 = load_image("images_project", "Rumah2.png", (LEBAR_RUMAH, TINGGI_RUMAH))
gambar_toko = load_image("images_project", "Toko.png", (LEBAR_RUMAH, TINGGI_RUMAH))
gambar_box = load_image("images_project", "Box.png", (UKURAN_UBIN, UKURAN_UBIN))
gambar_bangku = load_image("images_project", "Bangku.png", (UKURAN_UBIN*2, UKURAN_UBIN*3))
gambar_petunjukjalan = load_image("images_project", "PetunjukJalan.png", (UKURAN_UBIN, UKURAN_UBIN*3))
gambar_lampujalan = load_image("images_project", "LampuJalan.png", (UKURAN_UBIN, UKURAN_UBIN*3))
gambar_portal = load_image("images_project", "Portal.png", (64, 128))

# Ubin Peta
gambar_ubinlantai1 = load_image("images_project", "UbinLantai-1.png", (UKURAN_UBIN, UKURAN_UBIN))
gambar_ubintanah1 = load_image("images_project", "UbinTanah-1.png", (UKURAN_UBIN, UKURAN_UBIN))
gambar_ubinlantai2 = load_image("images_project", "UbinLantai-2.png", (UKURAN_UBIN, UKURAN_UBIN))
gambar_ubintanah2 = load_image("images_project", "UbinTanah-2.png", (UKURAN_UBIN, UKURAN_UBIN))
gambar_ubinlantai3 = load_image("images_project", "UbinLantai-3.png", (UKURAN_UBIN, UKURAN_UBIN))
gambar_ubintanah3 = load_image("images_project", "UbinTanah-3.png", (UKURAN_UBIN, UKURAN_UBIN))
gambar_ubinlantai4 = load_image("images_project", "UbinLantai-4.png", (UKURAN_UBIN, UKURAN_UBIN))
gambar_ubintanah4 = load_image("images_project", "UbinTanah-4.png", (UKURAN_UBIN, UKURAN_UBIN))

# ANIMASI MC BARU (Folder: images_mc, File Tanpa Inisial S)
gambar_MC_setup = [load_image("images_mc", f"MC-Setup{i}.png", (LEBAR_PEMAIN, TINGGI_PEMAIN)) for i in range(2)]
gambar_MC_jalankanan = [load_image("images_mc", f"MC-Jalankanan{i}.png", (LEBAR_PEMAIN, TINGGI_PEMAIN)) for i in range(4)]
gambar_MC_jalankiri = [load_image("images_mc", f"MC-JalanKiri{i}.png", (LEBAR_PEMAIN, TINGGI_PEMAIN)) for i in range(4)]
gambar_MC_lompatkanan = [load_image("images_mc", f"MC-LompatKanan{i}.png", (LEBAR_PEMAIN, TINGGI_PEMAIN)) for i in range(4)]
gambar_MC_lompatkiri = [load_image("images_mc", f"MC-LompatKiri{i}.png", (LEBAR_PEMAIN, TINGGI_PEMAIN)) for i in range(4)]
gambar_MC_serangankanan = [load_image("images_mc", f"MC-SerangKanan{i}.png", (LEBAR_PEMAIN, TINGGI_PEMAIN)) for i in range(4)]
gambar_MC_serangankiri = [load_image("images_mc", f"MC-SerangKiri{i}.png", (LEBAR_PEMAIN, TINGGI_PEMAIN)) for i in range(4)]

# Proyektil Angin Placeholder
gambar_angin = []
for i in range(4):
    try:
        img = load_image("images_project", "Skill-Angin.png", (128, 128))
        gambar_angin.append(img)
    except:
        surf = pygame.Surface((64, 64), pygame.SRCALPHA)
        pygame.draw.ellipse(surf, (135, 206, 250), (0, 16, 64, 32))
        gambar_angin.append(surf)

# PENGATURAN FONT
font_judul = pygame.font.Font("Font-Judul.ttf", 46)
font_petunjuk = pygame.font.Font("Font-Petunjuk.ttf", 16)

# PENGATURAN WINDOW
window = pygame.display.set_mode((LEBAR_CANVAS, TINGGI_CANVAS))
pygame.display.set_caption("ADVENTURE TO BECOME A KNIGHT")
pygame.display.set_icon(gambar_MC_setup[0])
clock = pygame.time.Clock()

# ==========================================
# KELAS ENEMY DUMMY & PROJECTILE
# ==========================================
class DummyMusuh(pygame.Rect):
    def __init__(self, x, y):
        pygame.Rect.__init__(self, x, y, 80, 100)
        self.hp = 100
        
    def terima_damage(self, jumlah_dmg):
        if self.hp > 0:
            self.hp -= jumlah_dmg
            print(f"Musuh1 terkena serang! Sisa HP: {self.hp}")
            if self.hp <= 0:
                print("Musuh1 Hancur!")

class ProyektilAngin(pygame.Rect):
    def __init__(self, x, y, arah):
        pygame.Rect.__init__(self, x, y, 64, 64)
        self.arah = arah
        self.kecepatan_x = 12 if arah == "right" else -12

    def update(self):
        self.x += self.kecepatan_x

# KELAS PEMAIN
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

# KELAS DEKORASI (OTOMATIS MENYESUAIKAN UKURAN DENGAN GAMBAR ASLI)
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
            # Bangunan
            elif abs(kode_map) == 12:
                posisi_y_pas = y + UKURAN_UBIN - 380
                rumah1.append(Rumah1(x, posisi_y_pas, gambar_rumah1))
            elif abs(kode_map) == 13:
                posisi_y_pas = y + UKURAN_UBIN - 380
                rumah1.append(Rumah1(x, posisi_y_pas, gambar_rumah2))
            elif abs(kode_map) == 14:
                posisi_y_pas = y + UKURAN_UBIN - 380
                rumah1.append(Rumah1(x, posisi_y_pas, gambar_toko))
            # Properti
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
            
def pindah_map(peta_baru, background_baru):
    global MAP_PERMAINAN, LEBAR_MAP, background_aktif, current_map_idx, musuh1
    MAP_PERMAINAN = peta_baru
    background_aktif = background_baru
    LEBAR_MAP = len(MAP_PERMAINAN[0]) * UKURAN_UBIN
    
    ubins.clear()
    ubin_background.clear()
    rumah1.clear()
    portals.clear()
    list_angin.clear()
    buat_map()
    
    if peta_baru == map_project.MAP2_PERMAINAN:
        current_map_idx = 2
        musuh1 = DummyMusuh(1300, TINGGI_CANVAS - 2 * UKURAN_UBIN - 100)
        mainkan_bgm("bgm_map2.mp3")
    else:
        current_map_idx = 1
        musuh1 = None
        mainkan_bgm("bgm_intro.mp3")
        
    pemain.x = 100 
    pemain.y = TINGGI_CANVAS - 2 * UKURAN_UBIN
    pemain.kecepatan_y = 0

def move():
    global kamera_x, game_state

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
                pemain.jalan = False
                pemain.kecepatan_x = 0
                game_state = "PROMPT" 

        kamera_x = pemain.x - (LEBAR_CANVAS / 2) + (pemain.width / 2)
        kamera_x = max(0, min(kamera_x, LEBAR_MAP - LEBAR_CANVAS))

    if game_state != "PROMPT" and game_state != "GAMEOVER": 
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
                    
        if pemain.y > TINGGI_CANVAS:
            pygame.mixer.music.stop()
            game_state = "GAMEOVER"

def draw():
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

    if current_map_idx == 2 and musuh1 and musuh1.hp > 0:
        pygame.draw.rect(window, (180, 40, 40), (musuh1.x - kamera_x, musuh1.y, musuh1.width, musuh1.height))
        teks_hp = font_petunjuk.render(f"Dummy HP: {musuh1.hp}/50", True, (255, 255, 255))
        window.blit(teks_hp, (musuh1.x - kamera_x, musuh1.y - 25))

    for angin in list_angin:
        frame_aktif = (pygame.time.get_ticks() // 100) % 4
        window.blit(gambar_angin[frame_aktif], (angin.x - kamera_x, angin.y))

    pemain.update_image() 
    window.blit(pemain.image, (pemain.x - kamera_x, pemain.y)) 

    # ==========================================
    # SISTEM TUTORIAL INTERAKTIF SEJAJAR MC (MELAYANG)
    # ==========================================
    if game_state == "PLAYING" and current_map_idx == 2:
        # Menentukan isi teks panduan berdasarkan koordinat X dari MC secara bertahap
        if pemain.x < 500:
            string_teks = "Tekan [A] atau [D] / Tombol Panah untuk jalan"
        elif 500 <= pemain.x < 950:
            string_teks = "Tekan [W] atau Panah Atas untuk melompat rintangan"
        elif 950 <= pemain.x < 1250:
            string_teks = "Dekati Target! Tekan [SPASI] untuk menyerang (10 DMG)"
        else:
            string_teks = "Coba KOMBO: Jalan Kanan + Tekan [SPASI] 2x untuk Lempar Angin!"

        # Render background balon teks kecil tepat diatas kepala MC
        teks_tutorial = font_petunjuk.render(string_teks, True, (0, 255, 100))
        lebar_t, tinggi_t = teks_tutorial.get_size()
        
        box_t_x = (pemain.x - kamera_x) + (pemain.width // 2) - (lebar_t // 2)
        box_t_y = pemain.y - 45
        
        # Gambar kotak background gelap tipis agar tulisan terbaca jelas di map manapun
        surf_bg = pygame.Surface((lebar_t + 16, tinggi_t + 8))
        surf_bg.fill((0, 0, 0))
        surf_bg.set_alpha(180)
        window.blit(surf_bg, (box_t_x - 8, box_t_y - 4))
        window.blit(teks_tutorial, (box_t_x, box_t_y))

    if game_state == "INTRO":
        teks_judul = font_judul.render("ADVENTURE TO BECOME A KNIGHT", True, ("Red"))
        rect_judul = teks_judul.get_rect(center=(LEBAR_CANVAS // 2, TINGGI_CANVAS // 3))
        rect_bayangan = rect_judul.copy()
        rect_bayangan.x += 3; rect_bayangan.y += 3
        window.blit(font_judul.render("ADVENTURE TO BECOME A KNIGHT", True, (0, 0, 0)), rect_bayangan)
        window.blit(teks_judul, rect_judul)
        
        if (pygame.time.get_ticks() // 500) % 2 == 0:
            teks_info = font_petunjuk.render("PRESS ENTER TO START GAME", True, ("Black"))
            rect_info = teks_info.get_rect(center=(LEBAR_CANVAS // 2, TINGGI_CANVAS // 2 + 30))
            window.blit(teks_info, rect_info)

    elif game_state == "PROMPT":
        lebar_box, tinggi_box = 550, 150
        box_x = (LEBAR_CANVAS - lebar_box) // 2
        box_y = (TINGGI_CANVAS - tinggi_box) // 2
        overlay = pygame.Surface((lebar_box, tinggi_box))
        overlay.set_alpha(220); overlay.fill((0, 0, 0))
        window.blit(overlay, (box_x, box_y))
        pygame.draw.rect(window, (255, 255, 255), (box_x, box_y, lebar_box, tinggi_box), 3)
        
        teks_tanya = font_petunjukrender = font_petunjuk.render("Mulai memainkan Sayembara sang putri?", True, (255, 255, 255))
        rect_tanya = teks_tanya.get_rect(center=(LEBAR_CANVAS // 2, box_y + 45))
        window.blit(teks_tanya, rect_tanya)
        
        teks_opsi = font_petunjuk.render("[Y] YES (Mulai)   /   [N] NO (Stay)", True, (255, 215, 0))
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


pemain = Pemain()
pemain.x = 100 

portals = []
rumah1 = []
ubins = []
ubin_background = []
list_angin = [] 
musuh1 = None

buat_map()
mainkan_bgm("bgm_intro.mp3") 

# GAME LOOP UTAMA
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER) and game_state == "INTRO":
                target_tengah_x = (LEBAR_CANVAS / 2) - (pemain.width / 2)
                jarak_ke_target = abs(pemain.x - target_tengah_x)
                if jarak_ke_target > 100:
                    pemain.x = target_tengah_x  
                    game_state = "PLAYING"      
                else:
                    game_state = "TRANSITION"   

            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER) and game_state == "GAMEOVER":
                game_state = "INTRO"
                pindah_map(map_project.MAP1_PERMAINAN, gambar_background1) 

            elif game_state == "PLAYING":
                if event.key == pygame.K_SPACE:
                    now = pygame.time.get_ticks()
                    keys = pygame.key.get_pressed()
                    
                    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
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
                        list_angin.append(ProyektilAngin(pemain.right, pemain.centery - 32, pemain.direction))
                        print("KOMBO AKTIF! Melempar Angin (20 DMG)!")
                        pemain.combo_count = 0 
                    else:
                        if not pemain.serang:
                            pemain.serang = True
                            pemain.current_frame = 0
                            print("MC Menyerang! Memberikan 10 DMG!")
                            if current_map_idx == 2 and musuh1 and musuh1.hp > 0:
                                if pemain.colliderect(musuh1):
                                    musuh1.terima_damage(10)

            elif game_state == "PROMPT":
                if event.key == pygame.K_y:
                    pindah_map(map_project.MAP2_PERMAINAN, gambar_background2) 
                    game_state = "PLAYING"
                                                            
                elif event.key == pygame.K_n:
                    game_state = "PLAYING"
                    if pemain.direction == "right":
                        pemain.x -= 60
                    else:
                        pemain.x += 60
    
    if game_state == "PLAYING":
        for angin in list_angin[:]:
            angin.update()
            if current_map_idx == 2 and musuh1 and musuh1.hp > 0:
                if angin.colliderect(musuh1):
                    musuh1.terima_damage(20) 
                    list_angin.remove(angin)
                    continue
            if angin.x - kamera_x > LEBAR_CANVAS or angin.x < 0 or angin.x > LEBAR_MAP:
                if angin in list_angin:
                    list_angin.remove(angin)

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