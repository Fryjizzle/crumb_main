#!/usr/bin/env python3
"""
🌀 Crumb UI - Minimal Sacred Interface v0.1
A clean, reliable menu system for continuous testing
Designed for RasPad touchscreen with sacred intention
"""

import tkinter as tk
from tkinter import font
import sys
import traceback
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
            
            # Setup fonts with error handling
            self.setup_fonts()
            
            # Create main container
            self.main_frame = tk.Frame(self.root, bg=self.colors['deep'])
            self.main_frame.pack(fill='both', expand=True)
            
            # Initialize screens
            self.screens = {}
            self.create_all_screens()
            
            # Show hub screen
            self.show_screen('hub')
            
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
        """🧿 The Sacred Hub - Gateway to all realms"""
        hub = tk.Frame(self.main_frame, bg=self.colors['deep'])
        
        # Title section
        title_frame = tk.Frame(hub, bg=self.colors['deep'])
        title_frame.pack(pady=40)
        
        title = tk.Label(title_frame, text="✧ CRUMB ✧", 
                        font=self.fonts['large_symbol'],
                        fg=self.colors['gold'],
                        bg=self.colors['deep'])
        title.pack()
        
        subtitle = tk.Label(title_frame, text="Sacred Companion • Testing Interface", 
                           font=self.fonts['subtitle'],
                           fg=self.colors['sage'],
                           bg=self.colors['deep'])
        subtitle.pack(pady=10)
        
        # Navigation grid
        nav_frame = tk.Frame(hub, bg=self.colors['deep'])
        nav_frame.pack(expand=True)
        
        # Sacred navigation buttons
        buttons = [
            ("🌍", "Elements", self.colors['earth'], 'elemental'),
            ("🎵", "Sounds", self.colors['ethereal'], 'soundboard'),
            ("🧙‍♂️", "Archetypes", self.colors['aether'], 'archetype'),
            ("⚙️", "Settings", self.colors['mystic'], 'settings')
        ]
        
        # Create 2x2 grid
        for i, (symbol, label, color, screen) in enumerate(buttons):
            row, col = i // 2, i % 2
            
            btn = tk.Button(nav_frame,
                           text=f"{symbol}\n{label}",
                           font=self.fonts['symbol'],
                           fg='white',
                           bg=color,
                           activebackground=self.adjust_color(color, 1.2),
                           activeforeground='white',
                           bd=0,
                           width=10,
                           height=4,
                           command=lambda s=screen: self.safe_navigate(s))
            btn.grid(row=row, column=col, padx=40, pady=30, sticky='nsew')
            
            # Configure grid weights
            nav_frame.grid_rowconfigure(row, weight=1)
            nav_frame.grid_columnconfigure(col, weight=1)
        
        self.screens['hub'] = hub

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
        """🎵 Sacred Soundboard - Expression tools (placeholder)"""
        soundboard = tk.Frame(self.main_frame, bg=self.colors['deep'])
        
        # Header
        self.create_header(soundboard, "✧ Sacred Sounds ✧", self.colors['ethereal'])
        
        # Content area
        content_frame = tk.Frame(soundboard, bg=self.colors['deep'])
        content_frame.pack(expand=True, fill='both', padx=40, pady=20)
        
        # Sound buttons grid
        sounds = [
            ("💚", "Happy", self.colors['sage']),
            ("😔", "Sad", self.colors['mystic']),
            ("😰", "Stress", self.colors['fire']),
            ("🤗", "Comfort", self.colors['water']),
            ("⚡", "Energy", self.colors['ethereal']),
            ("🌙", "Calm", self.colors['aether']),
            ("🍎", "Need", self.colors['earth']),
            ("💭", "Think", self.colors['air']),
            ("❤️", "Love", self.colors['gold'])
        ]
        
        for i, (emoji, label, color) in enumerate(sounds):
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
                           command=lambda l=label: self.play_sound_placeholder(l))
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

    def play_sound_placeholder(self, sound_name):
        """🎵 Placeholder sound playing"""
        try:
            print(f"♫ Playing {sound_name} sound ♫")
            self.show_temporary_message(f"♫ {sound_name} ♫\nSound Played", self.colors['ethereal'])
        except Exception as e:
            print(f"Sound play error: {e}")

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
            self.root.quit()
        except:
            print("✧ Force closing ✧")
            sys.exit(0)

    def run(self):
        """🌀 Begin the sacred journey with robust error handling"""
        try:
            print("✧ Crumb UI v0.1 - Sacred Interface Starting ✧")
            print("Triple-tap top-left corner to exit")
            
            # Set up global error handler
            def handle_tk_error(error):
                self.handle_critical_error("Tkinter", error)
                return True
            
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
