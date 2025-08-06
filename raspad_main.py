#!/usr/bin/env python3
"""
🌀 Crumb UI - Minimal Sacred Interface v0.1
A clean, reliable menu system with music and sounds
Designed for RasPad touchscreen with sacred intention
"""

import tkinter as tk
from tkinter import font
import sys
import traceback
import math
import random
import pygame
import os
from datetime import datetime

class CrumbUI:
    def __init__(self):
        try:
            # Initialize the sacred vessel (main window)
            self.root = tk.Tk()
            self.root.title("✧ Crumb ✧")
            self.root.configure(bg='#1a1a2e')
            
            # Configure for touchscreen (RasPad dimensions)
            self.root.geometry("1024x600")
            self.root.attributes('-fullscreen', True)
            
            # Sacred color palette - simplified
            self.colors = {
                'void': '#0f0f23',
                'deep': '#1a1a2e', 
                'mystic': '#16213e',
                'ethereal': '#e94560',
                'gold': '#f3a712',
                'sage': '#53a8b6',
                'earth': '#8b5a3c',
                'fire': '#ff6b35',
                'water': '#4ecdc4',
                'air': '#95e1d3',
                'aether': '#c44569'
            }
            
            # Initialize app state
            self.current_screen = "hub"
            self.last_activity = datetime.now()
            
            # Setup fonts and audio
            self.setup_fonts()
            self.setup_audio()
            
            # Create main container
            self.main_frame = tk.Frame(self.root, bg=self.colors['deep'])
            self.main_frame.pack(fill='both', expand=True)
            
            # Initialize screens
            self.screens = {}
            self.create_all_screens()
            
            # Show hub screen
            self.show_screen('hub')
            
            # Play startup music
            self.play_startup_music()
            
            # Bind exit gesture and error handling
            self.exit_taps = 0
            self.root.bind('<Button-1>', self.handle_click)
            
            # Set up continuous operation
            self.setup_continuous_operation()
            
            print("✧ Crumb UI initialized successfully ✧")
            
        except Exception as e:
            self.handle_critical_error("Initialization", e)

    def setup_fonts(self):
        """Initialize sacred typography with fallbacks"""
        try:
            self.fonts = {
                'title': font.Font(family="Arial", size=24, weight="bold"),
                'subtitle': font.Font(family="Arial", size=16),
                'body': font.Font(family="Arial", size=12),
                'symbol': font.Font(family="Arial", size=20, weight="bold"),
                'large_symbol': font.Font(family="Arial", size=36, weight="bold")
            }
        except Exception as e:
            print(f"Font setup warning: {e}")
            # Fallback to default fonts
            self.fonts = {
                'title': ('Arial', 24, 'bold'),
                'subtitle': ('Arial', 16),
                'body': ('Arial', 12),
                'symbol': ('Arial', 20, 'bold'),
                'large_symbol': ('Arial', 36, 'bold')
            }

    def setup_audio(self):
        """Initialize audio system"""
        try:
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
            self.audio_enabled = True
            print("✧ Audio system initialized ✧")
        except Exception as e:
            print(f"Audio initialization error: {e}")
            self.audio_enabled = False

    def play_startup_music(self):
        """Play mystical startup music"""
        if not self.audio_enabled:
            return
        try:
            music_file = "assets/sounds/startup_mystical.wav"
            if os.path.exists(music_file):
                pygame.mixer.music.load(music_file)
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1)  # Loop forever
                print("✧ Startup music playing ✧")
            else:
                print(f"Startup music not found: {music_file}")
        except Exception as e:
            print(f"Music play error: {e}")

    def play_sound(self, sound_name):
        """Play individual sound effects"""
        if not self.audio_enabled:
            return
        try:
            sound_file = f"assets/sounds/{sound_name}.wav"
            if os.path.exists(sound_file):
                sound = pygame.mixer.Sound(sound_file)
                sound.play()
                print(f"✧ Playing {sound_name} ✧")
            else:
                print(f"Sound not found: {sound_file}")
                # Play placeholder beep
                self.play_placeholder_beep()
        except Exception as e:
            print(f"Sound play error: {e}")

    def play_placeholder_beep(self):
        """Generate a simple beep for missing sounds"""
        print("♫ Beep! (placeholder sound) ♫")

    def create_all_screens(self):
        """Create all interface screens with error handling"""
        screen_creators = [
            ('hub', self.create_hub_screen),
            ('elemental', self.create_elemental_screen),
            ('soundboard', self.create_soundboard_screen),
            ('archetype', self.create_archetype_screen),
            ('settings', self.create_settings_screen)
        ]
        
        for screen_name, creator_func in screen_creators:
            try:
                creator_func()
                print(f"✧ Created {screen_name} screen ✧")
            except Exception as e:
                print(f"Error creating {screen_name} screen: {e}")
                self.create_error_screen(screen_name, e)

    def create_hub_screen(self):
        """🧿 The Sacred Hub - Gateway to all realms with mystical animations"""
        hub = tk.Frame(self.main_frame, bg=self.colors['void'])
        
        # Animated background canvas
        self.hub_canvas = tk.Canvas(hub, bg=self.colors['void'], highlightthickness=0)
        self.hub_canvas.pack(fill='both', expand=True)
        
        # Create mystical background elements
        self.create_mystical_background()
        
        # Floating title with glow effect
        title_y = 80
        # Create glow layers for depth
        for i in range(5, 0, -1):
            glow_size = 36 + (i * 3)  # Base size + glow increment
            self.hub_canvas.create_text(512, title_y, text="✧ CRUMB ✧",
                                      font=('Arial', glow_size, 'bold'),
                                      fill=self.colors['gold'], anchor='center')
        
        # Main title
        self.hub_canvas.create_text(512, title_y, text="✧ CRUMB ✧",
                                  font=('Arial', 36, 'bold'),
                                  fill=self.colors['ethereal'], anchor='center')
        
        # Subtitle with mystical particles
        subtitle_y = title_y + 60
        self.hub_canvas.create_text(512, subtitle_y, 
                                  text="Sacred Companion • Mystical Interface",
                                  font=('Arial', 16),
                                  fill=self.colors['sage'], anchor='center')
        
        # Create floating navigation orbs instead of buttons
        self.create_navigation_orbs()
        
        # Start ambient animations
        self.start_hub_animations()
        
        self.screens['hub'] = hub

    def create_mystical_background(self):
        """Create animated background with floating particles and energy lines"""
        # Create floating mystical symbols
        symbols = ['✧', '◊', '○', '△', '◇', '☽', '☾', '✦', '✧']
        self.background_elements = []
        
        for i in range(25):
            x = random.randint(50, 974)
            y = random.randint(50, 550)
            symbol = random.choice(symbols)
            size = random.randint(12, 24)
            alpha = random.choice(['#16213e', '#0f0f23', '#1a1a2e'])
            
            element_id = self.hub_canvas.create_text(x, y, text=symbol,
                                                   font=('Arial', size),
                                                   fill=alpha, anchor='center')
            
            self.background_elements.append({
                'id': element_id,
                'x': x, 'y': y,
                'dx': random.uniform(-0.5, 0.5),
                'dy': random.uniform(-0.3, 0.3),
                'phase': random.uniform(0, 6.28)
            })
        
        # Create energy connecting lines
        self.energy_lines = []
        for i in range(8):
            x1, y1 = random.randint(0, 1024), random.randint(0, 600)
            x2, y2 = random.randint(0, 1024), random.randint(0, 600)
            line_id = self.hub_canvas.create_line(x1, y1, x2, y2,
                                                fill=self.colors['mystic'],
                                                width=1, smooth=True)
            self.energy_lines.append({
                'id': line_id,
                'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2,
                'phase': random.uniform(0, 6.28)
            })

    def create_navigation_orbs(self):
        """Create beautiful floating orb navigation instead of rectangular buttons"""
        # Central mystical pattern
        center_x, center_y = 512, 350
        
        # Navigation orbs data
        orbs = [
            ("🌍", "Elements", self.colors['earth'], 'elemental', -120, -80),
            ("🎵", "Sounds", self.colors['ethereal'], 'soundboard', 120, -80),
            ("🧙‍♂️", "Archetypes", self.colors['aether'], 'archetype', -120, 80),
            ("⚙️", "Settings", self.colors['mystic'], 'settings', 120, 80)
        ]
        
        self.nav_orbs = []
        
        for symbol, label, color, screen, offset_x, offset_y in orbs:
            orb_x = center_x + offset_x
            orb_y = center_y + offset_y
            
            # Create orb glow (multiple layers for depth)
            glow_radius = 75
            for i in range(5, 0, -1):
                glow_size = glow_radius + (i * 8)
                glow_color = self.adjust_color(color, 0.3 + (i * 0.1))
                glow_id = self.hub_canvas.create_oval(orb_x - glow_size//2, orb_y - glow_size//2,
                                                    orb_x + glow_size//2, orb_y + glow_size//2,
                                                    fill=glow_color, outline='', stipple='gray25')
            
            # Main orb
            orb_id = self.hub_canvas.create_oval(orb_x - 50, orb_y - 50,
                                               orb_x + 50, orb_y + 50,
                                               fill=color, outline=self.colors['gold'], width=2)
            
            # Symbol
            symbol_id = self.hub_canvas.create_text(orb_x, orb_y - 5, text=symbol,
                                                  font=('Arial', 28, 'bold'),
                                                  fill='white', anchor='center')
            
            # Label
            label_id = self.hub_canvas.create_text(orb_x, orb_y + 80, text=label,
                                                 font=self.fonts['subtitle'],
                                                 fill=color, anchor='center')
            
            # Store orb data for animations and clicks
            orb_data = {
                'orb_id': orb_id, 'symbol_id': symbol_id, 'label_id': label_id,
                'x': orb_x, 'y': orb_y, 'base_x': orb_x, 'base_y': orb_y,
                'color': color, 'screen': screen, 'phase': random.uniform(0, 6.28),
                'hover_scale': 1.0, 'pulse_phase': random.uniform(0, 6.28)
            }
            self.nav_orbs.append(orb_data)
            
            # Bind click events
            self.hub_canvas.tag_bind(orb_id, '<Button-1>', 
                                   lambda e, s=screen: self.orb_click_effect(s))
            self.hub_canvas.tag_bind(symbol_id, '<Button-1>', 
                                   lambda e, s=screen: self.orb_click_effect(s))
        
        # Central mystical core
        core_radius = 40
        self.hub_canvas.create_oval(center_x - core_radius, center_y - core_radius,
                                  center_x + core_radius, center_y + core_radius,
                                  fill=self.colors['void'], outline=self.colors['gold'], width=3)
        
        # Rotating mystical symbol in center
        self.central_symbol = self.hub_canvas.create_text(center_x, center_y, text="✧",
                                                        font=('Arial', 32, 'bold'),
                                                        fill=self.colors['gold'], anchor='center')

    def start_hub_animations(self):
        """Start all the beautiful ambient animations"""
        self.animate_background()
        self.animate_orbs()
        self.animate_central_core()

    def animate_background(self):
        """Animate floating background elements"""
        try:
            import math
            
            for element in self.background_elements:
                # Update position with gentle floating motion
                element['x'] += element['dx']
                element['y'] += element['dy'] + math.sin(element['phase']) * 0.2
                element['phase'] += 0.02
                
                # Wrap around screen edges
                if element['x'] < 0: element['x'] = 1024
                if element['x'] > 1024: element['x'] = 0
                if element['y'] < 0: element['y'] = 600
                if element['y'] > 600: element['y'] = 0
                
                # Update canvas position
                self.hub_canvas.coords(element['id'], element['x'], element['y'])
            
            # Animate energy lines with gentle pulsing
            for line in self.energy_lines:
                line['phase'] += 0.03
                alpha_factor = 0.5 + 0.3 * math.sin(line['phase'])
                # Note: Tkinter doesn't support alpha on lines, so we simulate with color intensity
            
            # Continue animation
            if hasattr(self, 'hub_canvas') and self.current_screen == 'hub':
                self.root.after(50, self.animate_background)
                
        except Exception as e:
            print(f"Background animation error: {e}")

    def animate_orbs(self):
        """Animate navigation orbs with floating and pulsing effects"""
        try:
            import math
            
            for orb in self.nav_orbs:
                # Gentle floating motion
                orb['phase'] += 0.02
                float_y = orb['base_y'] + math.sin(orb['phase']) * 8
                float_x = orb['base_x'] + math.cos(orb['phase'] * 0.7) * 3
                
                # Pulsing glow effect
                orb['pulse_phase'] += 0.05
                pulse_scale = 1.0 + math.sin(orb['pulse_phase']) * 0.1
                
                # Update orb position
                self.hub_canvas.coords(orb['orb_id'], 
                                     float_x - 50 * pulse_scale, float_y - 50 * pulse_scale,
                                     float_x + 50 * pulse_scale, float_y + 50 * pulse_scale)
                
                # Update symbol position
                self.hub_canvas.coords(orb['symbol_id'], float_x, float_y - 5)
                
                # Update label position
                self.hub_canvas.coords(orb['label_id'], float_x, float_y + 80)
            
            # Continue animation
            if hasattr(self, 'hub_canvas') and self.current_screen == 'hub':
                self.root.after(30, self.animate_orbs)
                
        except Exception as e:
            print(f"Orb animation error: {e}")

    def animate_central_core(self):
        """Animate the central mystical symbol with rotation"""
        try:
            import math
            
            # Rotate the central symbol
            if hasattr(self, 'central_symbol'):
                symbols = ['✧', '◊', '✦', '◇', '✧']
                current_time = datetime.now().second
                symbol_index = (current_time // 2) % len(symbols)
                
                self.hub_canvas.itemconfig(self.central_symbol, text=symbols[symbol_index])
            
            # Continue animation
            if hasattr(self, 'hub_canvas') and self.current_screen == 'hub':
                self.root.after(1000, self.animate_central_core)
                
        except Exception as e:
            print(f"Central core animation error: {e}")

    def orb_click_effect(self, screen_name):
        """Create magical click effect and navigate"""
        try:
            # Create ripple effect at click
            self.create_click_ripple()
            
            # Navigate after brief delay for effect
            self.root.after(200, lambda: self.safe_navigate(screen_name))
            
        except Exception as e:
            print(f"Orb click error: {e}")

    def create_click_ripple(self):
        """Create beautiful ripple effect on orb click"""
        try:
            center_x, center_y = 512, 350
            
            # Create expanding ripples
            for i in range(3):
                delay = i * 100
                self.root.after(delay, lambda i=i: self.draw_ripple(center_x, center_y, i))
                
        except Exception as e:
            print(f"Ripple effect error: {e}")

    def draw_ripple(self, x, y, wave_num):
        """Draw a single ripple wave"""
        try:
            initial_radius = 20 + (wave_num * 15)
            max_radius = 150
            
            def expand_ripple(radius):
                if radius > max_radius:
                    return
                    
                # Draw ripple circle
                ripple_id = self.hub_canvas.create_oval(x - radius, y - radius,
                                                      x + radius, y + radius,
                                                      outline=self.colors['gold'],
                                                      width=2, fill='')
                
                # Remove ripple after short time and continue expansion
                self.root.after(50, lambda: self.hub_canvas.delete(ripple_id))
                self.root.after(20, lambda: expand_ripple(radius + 8))
            
            expand_ripple(initial_radius)
            
        except Exception as e:
            print(f"Ripple draw error: {e}")

    def create_elemental_screen(self):
        """🌱 Elemental Modes - Sacred forces (placeholder)"""
        elemental = tk.Frame(self.main_frame, bg=self.colors['void'])
        
        # Header with back button
        self.create_header(elemental, "✧ Elemental Modes ✧", self.colors['gold'])
        
        # Content area
        content_frame = tk.Frame(elemental, bg=self.colors['void'])
        content_frame.pack(expand=True, fill='both', padx=40, pady=20)
        
        # Elements grid
        elements = [
            ("🌍", "Earth", self.colors['earth']),
            ("🔥", "Fire", self.colors['fire']),
            ("🌊", "Water", self.colors['water']),
            ("💨", "Air", self.colors['air']),
            ("✨", "Aether", self.colors['aether'])
        ]
        
        for i, (symbol, name, color) in enumerate(elements):
            row, col = i // 3, i % 3
            
            element_frame = tk.Frame(content_frame, bg=self.colors['void'])
            element_frame.grid(row=row, column=col, padx=30, pady=30, sticky='nsew')
            
            # Element button
            btn = tk.Button(element_frame,
                           text=symbol,
                           font=self.fonts['large_symbol'],
                           fg='white',
                           bg=color,
                           activebackground=self.adjust_color(color, 1.2),
                           width=4,
                           height=2,
                           bd=0,
                           command=lambda n=name: self.activate_element(n))
            btn.pack()
            
            # Element name
            name_label = tk.Label(element_frame, 
                                 text=name,
                                 font=self.fonts['subtitle'],
                                 fg=color,
                                 bg=self.colors['void'])
            name_label.pack(pady=10)
        
        # Configure grid
        for i in range(2):
            content_frame.grid_rowconfigure(i, weight=1)
        for i in range(3):
            content_frame.grid_columnconfigure(i, weight=1)
        
        self.screens['elemental'] = elemental

    def create_soundboard_screen(self):
        """🎵 Sacred Soundboard - Expression tools with real sounds"""
        soundboard = tk.Frame(self.main_frame, bg=self.colors['deep'])
        
        # Header
        self.create_header(soundboard, "✧ Sacred Sounds ✧", self.colors['ethereal'])
        
        # Content area
        content_frame = tk.Frame(soundboard, bg=self.colors['deep'])
        content_frame.pack(expand=True, fill='both', padx=40, pady=20)
        
        # Sound buttons grid - 9 sounds ready for MP3 files
        sounds = [
            ("💚", "Happy", self.colors['sage'], "happy"),
            ("😔", "Sad", self.colors['mystic'], "sad"),
            ("😰", "Stress", self.colors['fire'], "stress"),
            ("🤗", "Comfort", self.colors['water'], "comfort"),
            ("⚡", "Energy", self.colors['ethereal'], "energy"),
            ("🌙", "Calm", self.colors['aether'], "calm"),
            ("🍎", "Need", self.colors['earth'], "need"),
            ("💭", "Think", self.colors['air'], "think"),
            ("❤️", "Love", self.colors['gold'], "love")
        ]
        
        for i, (emoji, label, color, sound_file) in enumerate(sounds):
            row, col = i // 3, i % 3
            
            btn = tk.Button(content_frame,
                           text=f"{emoji}\n{label}",
                           font=self.fonts['symbol'],
                           fg='white',
                           bg=color,
                           activebackground=self.adjust_color(color, 1.2),
                           width=8,
                           height=3,
                           bd=0,
                           command=lambda f=sound_file: self.play_sound(f))
            btn.grid(row=row, column=col, padx=20, pady=15, sticky='nsew')
        
        # Configure grid
        for i in range(3):
            content_frame.grid_rowconfigure(i, weight=1)
            content_frame.grid_columnconfigure(i, weight=1)
        
        self.screens['soundboard'] = soundboard

    def create_archetype_screen(self):
        """🧙‍♂️ Archetype Portal - Future companions"""
        archetype = tk.Frame(self.main_frame, bg=self.colors['void'])
        
        # Header
        self.create_header(archetype, "✧ Archetype Portal ✧", self.colors['aether'])
        
        # Content area
        content_frame = tk.Frame(archetype, bg=self.colors['void'])
        content_frame.pack(expand=True)
        
        # Future content placeholder
        symbol = tk.Label(content_frame, 
                         text="🔮",
                         font=self.fonts['large_symbol'],
                         fg=self.colors['aether'],
                         bg=self.colors['void'])
        symbol.pack(pady=60)
        
        message = tk.Label(content_frame, 
                          text="Sacred Archetypes Awakening...\n\n• The Guide\n• The Trickster\n• The Watcher\n• The Healer\n\nComing Soon",
                          font=self.fonts['subtitle'],
                          fg=self.colors['sage'],
                          bg=self.colors['void'],
                          justify='center')
        message.pack()
        
        self.screens['archetype'] = archetype

    def create_settings_screen(self):
        """⚙️ Sacred Settings - Configuration"""
        settings = tk.Frame(self.main_frame, bg=self.colors['mystic'])
        
        # Header
        self.create_header(settings, "✧ Sacred Settings ✧", self.colors['gold'])
        
        # Content area
        content_frame = tk.Frame(settings, bg=self.colors['mystic'])
        content_frame.pack(expand=True, pady=40)
        
        # Settings options
        settings_items = [
            ("🔊", "Volume", "Adjust sound levels"),
            ("✨", "Brightness", "Screen brightness"),
            ("🎨", "Theme", "Color preferences"),
            ("🔄", "Reset", "Restore defaults"),
            ("ℹ️", "About", "System information"),
            ("🚪", "Exit", "Close application")
        ]
        
        for i, (symbol, title, desc) in enumerate(settings_items):
            row, col = i // 2, i % 2
            
            setting_frame = tk.Frame(content_frame, bg=self.colors['mystic'])
            setting_frame.grid(row=row, column=col, padx=40, pady=20, sticky='ew')
            
            btn = tk.Button(setting_frame,
                           text=f"{symbol} {title}",
                           font=self.fonts['subtitle'],
                           fg='white',
                           bg=self.colors['deep'],
                           activebackground=self.adjust_color(self.colors['deep'], 1.3),
                           bd=0,
                           width=15,
                           height=2,
                           command=lambda t=title: self.handle_setting(t))
            btn.pack()
            
            desc_label = tk.Label(setting_frame,
                                 text=desc,
                                 font=self.fonts['body'],
                                 fg=self.colors['sage'],
                                 bg=self.colors['mystic'])
            desc_label.pack(pady=5)
        
        # Configure grid
        for i in range(3):
            content_frame.grid_rowconfigure(i, weight=1)
        for i in range(2):
            content_frame.grid_columnconfigure(i, weight=1)
        
        self.screens['settings'] = settings

    def create_header(self, parent, title_text, title_color):
        """Create a standard header with back button"""
        header = tk.Frame(parent, bg=parent['bg'])
        header.pack(fill='x', pady=20)
        
        # Back button
        back_btn = tk.Button(header, 
                            text="← Hub",
                            font=self.fonts['body'],
                            fg=self.colors['sage'],
                            bg=self.colors['deep'],
                            activebackground=self.adjust_color(self.colors['deep'], 1.2),
                            bd=0,
                            padx=20,
                            pady=10,
                            command=lambda: self.safe_navigate('hub'))
        back_btn.pack(side='left', padx=20)
        
        # Title
        title = tk.Label(header, 
                        text=title_text,
                        font=self.fonts['title'],
                        fg=title_color,
                        bg=parent['bg'])
        title.pack()

    def create_error_screen(self, screen_name, error):
        """Create a fallback error screen"""
        error_screen = tk.Frame(self.main_frame, bg=self.colors['deep'])
        
        error_label = tk.Label(error_screen,
                              text=f"⚠️ Error in {screen_name}\n\n{str(error)[:100]}...\n\nReturning to Hub",
                              font=self.fonts['subtitle'],
                              fg=self.colors['ethereal'],
                              bg=self.colors['deep'],
                              justify='center')
        error_label.pack(expand=True)
        
        # Auto-return to hub after 3 seconds
        error_screen.after(3000, lambda: self.safe_navigate('hub'))
        
        self.screens[screen_name] = error_screen

    def safe_navigate(self, screen_name):
        """Navigate with error handling"""
        try:
            self.show_screen(screen_name)
            self.last_activity = datetime.now()
            print(f"✧ Navigated to {screen_name} ✧")
        except Exception as e:
            print(f"Navigation error to {screen_name}: {e}")
            self.show_screen('hub')

    def show_screen(self, screen_name):
        """Navigate between sacred realms"""
        # Hide all screens
        for screen in self.screens.values():
            screen.pack_forget()
        
        # Show requested screen or default to hub
        target_screen = screen_name if screen_name in self.screens else 'hub'
        self.screens[target_screen].pack(fill='both', expand=True)
        self.current_screen = target_screen

    def activate_element(self, element_name):
        """🌱 Placeholder element activation"""
        try:
            print(f"✧ Activating {element_name} mode ✧")
            self.show_temporary_message(f"✨ {element_name} ✨\nActivated", self.colors['gold'])
        except Exception as e:
            print(f"Element activation error: {e}")

    def handle_setting(self, setting_name):
        """⚙️ Placeholder settings handler"""
        try:
            if setting_name == "Exit":
                self.graceful_exit()
            else:
                print(f"⚙️ {setting_name} setting accessed ⚙️")
                self.show_temporary_message(f"⚙️ {setting_name} ⚙️\nComing Soon", self.colors['sage'])
        except Exception as e:
            print(f"Settings error: {e}")

    def show_temporary_message(self, message, color):
        """Show a temporary overlay message"""
        try:
            overlay = tk.Toplevel(self.root)
            overlay.configure(bg=self.colors['void'])
            overlay.attributes('-fullscreen', True)
            overlay.attributes('-alpha', 0.9)
            
            message_label = tk.Label(overlay,
                                   text=message,
                                   font=self.fonts['title'],
                                   fg=color,
                                   bg=self.colors['void'])
            message_label.pack(expand=True)
            
            # Auto-close after 1.5 seconds
            overlay.after(1500, overlay.destroy)
            
        except Exception as e:
            print(f"Overlay error: {e}")

    def handle_click(self, event):
        """Handle all click events including exit gesture"""
        try:
            self.last_activity = datetime.now()
            
            # Exit gesture: triple-tap top-left corner
            if event.x < 100 and event.y < 100:
                self.exit_taps += 1
                if self.exit_taps >= 3:
                    self.graceful_exit()
                # Reset counter after 2 seconds
                self.root.after(2000, self.reset_exit_counter)
                
        except Exception as e:
            print(f"Click handler error: {e}")

    def reset_exit_counter(self):
        """Reset the exit gesture counter"""
        self.exit_taps = 0

    def adjust_color(self, hex_color, factor):
        """Adjust color brightness for hover effects"""
        try:
            hex_color = hex_color.lstrip('#')
            rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            adjusted_rgb = tuple(min(255, max(0, int(c * factor))) for c in rgb)
            return f"#{adjusted_rgb[0]:02x}{adjusted_rgb[1]:02x}{adjusted_rgb[2]:02x}"
        except:
            return hex_color  # Return original on error

    def setup_continuous_operation(self):
        """Set up continuous operation with error recovery"""
        def heartbeat():
            try:
                # Update UI every second
                self.root.after(1000, heartbeat)
            except Exception as e:
                print(f"Heartbeat error: {e}")
                # Try to recover
                self.root.after(5000, heartbeat)
        
        # Start heartbeat
        heartbeat()

    def handle_critical_error(self, context, error):
        """Handle critical errors that could crash the app"""
        error_msg = f"Critical error in {context}: {str(error)}"
        print(f"🚨 {error_msg}")
        print(f"Traceback: {traceback.format_exc()}")
        
        try:
            # Try to show error on screen
            if hasattr(self, 'root') and self.root.winfo_exists():
                error_label = tk.Label(self.root,
                                     text=f"🚨 System Error\n\n{error_msg[:200]}...\n\nContinuing...",
                                     font=('Arial', 16),
                                     fg='#ff6b35',
                                     bg='#1a1a2e')
                error_label.pack(expand=True)
                self.root.after(5000, error_label.destroy)
        except:
            pass  # If we can't show the error, just continue

    def graceful_exit(self):
        """🚪 Exit the sacred space gracefully"""
        try:
            print("✧ Sacred journey ending gracefully ✧")
            if self.audio_enabled:
                pygame.mixer.quit()
            self.root.quit()
        except:
            print("✧ Force closing ✧")
            sys.exit(0)

    def run(self):
        """🌀 Begin the sacred journey with robust error handling"""
        try:
            print("✧ Crumb UI v0.1 - Sacred Interface Starting ✧")
            print("Triple-tap top-left corner to exit")
            
            # Start the main loop with error handling
            while True:
                try:
                    self.root.mainloop()
                    break  # Normal exit
                except Exception as e:
                    self.handle_critical_error("Main Loop", e)
                    # Try to recover
                    if hasattr(self, 'root'):
                        try:
                            self.root.update()
                        except:
                            break
                    else:
                        break
                        
        except KeyboardInterrupt:
            print("\n✧ Sacred journey interrupted by user ✧")
        except Exception as e:
            self.handle_critical_error("Application", e)
        finally:
            print("✧ Crumb UI session ended ✧")


def main():
    """Initialize the sacred vessel with maximum reliability"""
    try:
        app = CrumbUI() 
        app.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        print(f"Traceback: {traceback.format_exc()}")
        # Keep the process alive even on fatal errors
        print("✧ Attempting emergency recovery ✧")
        try:
            # Basic emergency interface
            root = tk.Tk()
            root.configure(bg='#1a1a2e')
            root.attributes('-fullscreen', True)
            
            error_msg = tk.Label(root,
                               text="🚨 Emergency Mode 🚨\n\nCrumb encountered an error\nbut is still running\n\nTriple-tap corners to exit",
                               font=('Arial', 20),
                               fg='#f3a712',
                               bg='#1a1a2e')
            error_msg.pack(expand=True)
            
            def emergency_exit(event):
                if event.x < 100 or event.x > 924:
                    if event.y < 100 or event.y > 500:
                        root.quit()
            
            root.bind('<Button-1>', emergency_exit)
            root.mainloop()
            
        except:
            print("✧ Emergency recovery failed - system exit ✧")


if __name__ == "__main__":
    main()
