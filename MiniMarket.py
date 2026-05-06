"""
=============================================================
  TPS - SISTEMA DE PUNTO DE VENTA
  MiniMarket "QuickShop"
  Materia: Sistemas de Información
  Versión 2.0 — Con gestión de stock en tiempo real
=============================================================
"""

import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime

ARCHIVO_TRANSACCIONES = "transacciones.csv"
ARCHIVO_DETALLES      = "detalles_venta.csv"
ARCHIVO_INVENTARIO    = "inventario.csv"

BG_OSCURO  = "#0d1117"
BG_PANEL   = "#161b27"
BG_CARD    = "#1e2536"
AZUL       = "#4f8ef7"
AZUL_OSC   = "#3a6ed8"
VERDE      = "#22c55e"
VERDE_OSC  = "#16a34a"
ROJO       = "#ef4444"
AMARILLO   = "#f59e0b"
BLANCO     = "#e2e8f0"
GRIS       = "#64748b"
BORDE      = "#2a3350"

F_TITULO   = ("Consolas", 12, "bold")
F_NORMAL   = ("Consolas", 10)
F_CHICA    = ("Consolas", 9)

CATALOGO_BASE = [
    {"codigo":"B001","nombre":"Agua mineral 500ml",       "precio":0.50, "stock":150,"categoria":"Bebidas"},
    {"codigo":"B002","nombre":"Agua con gas 500ml",        "precio":0.65, "stock":80, "categoria":"Bebidas"},
    {"codigo":"B003","nombre":"Coca-Cola 600ml",           "precio":1.25, "stock":100,"categoria":"Bebidas"},
    {"codigo":"B004","nombre":"Coca-Cola 1.5L",            "precio":1.80, "stock":70, "categoria":"Bebidas"},
    {"codigo":"B005","nombre":"Sprite 600ml",              "precio":1.20, "stock":90, "categoria":"Bebidas"},
    {"codigo":"B006","nombre":"Fanta naranja 600ml",       "precio":1.20, "stock":85, "categoria":"Bebidas"},
    {"codigo":"B007","nombre":"Jugo del Valle naranja 1L", "precio":1.50, "stock":60, "categoria":"Bebidas"},
    {"codigo":"B008","nombre":"Jugo de mango 500ml",       "precio":1.10, "stock":55, "categoria":"Bebidas"},
    {"codigo":"B009","nombre":"Energizante Monster 473ml", "precio":2.50, "stock":40, "categoria":"Bebidas"},
    {"codigo":"B010","nombre":"Gatorade 600ml",            "precio":1.30, "stock":65, "categoria":"Bebidas"},
    {"codigo":"B011","nombre":"Te helado limon 500ml",     "precio":1.00, "stock":75, "categoria":"Bebidas"},
    {"codigo":"B012","nombre":"Leche entera 1L",           "precio":0.95, "stock":80, "categoria":"Bebidas"},
    {"codigo":"B013","nombre":"Leche deslactosada 1L",     "precio":1.20, "stock":50, "categoria":"Bebidas"},
    {"codigo":"S001","nombre":"Papas Lays 90g",            "precio":1.10, "stock":90, "categoria":"Snacks"},
    {"codigo":"S002","nombre":"Papas Ruffles 90g",         "precio":1.10, "stock":85, "categoria":"Snacks"},
    {"codigo":"S003","nombre":"Doritos 90g",               "precio":1.20, "stock":95, "categoria":"Snacks"},
    {"codigo":"S004","nombre":"Cheetos 80g",               "precio":1.00, "stock":70, "categoria":"Snacks"},
    {"codigo":"S005","nombre":"Galletas Oreo 120g",        "precio":1.50, "stock":60, "categoria":"Snacks"},
    {"codigo":"S006","nombre":"Galletas de vainilla 100g", "precio":0.90, "stock":65, "categoria":"Snacks"},
    {"codigo":"S007","nombre":"Chifles 80g",               "precio":0.75, "stock":80, "categoria":"Snacks"},
    {"codigo":"S008","nombre":"Mani con chocolate 50g",    "precio":0.80, "stock":70, "categoria":"Snacks"},
    {"codigo":"S009","nombre":"Barra de cereal 35g",       "precio":0.60, "stock":90, "categoria":"Snacks"},
    {"codigo":"S010","nombre":"Chocolatin 40g",            "precio":0.70, "stock":100,"categoria":"Snacks"},
    {"codigo":"L001","nombre":"Yogur natural 200g",        "precio":0.75, "stock":50, "categoria":"Lacteos"},
    {"codigo":"L002","nombre":"Yogur fresa 200g",          "precio":0.80, "stock":45, "categoria":"Lacteos"},
    {"codigo":"L003","nombre":"Queso fresco 250g",         "precio":1.80, "stock":35, "categoria":"Lacteos"},
    {"codigo":"L004","nombre":"Queso mozzarella 200g",     "precio":2.20, "stock":30, "categoria":"Lacteos"},
    {"codigo":"L005","nombre":"Mantequilla 100g",          "precio":1.50, "stock":40, "categoria":"Lacteos"},
    {"codigo":"L006","nombre":"Huevos x12",                "precio":2.50, "stock":50, "categoria":"Lacteos"},
    {"codigo":"L007","nombre":"Crema de leche 250ml",      "precio":1.20, "stock":35, "categoria":"Lacteos"},
    {"codigo":"P001","nombre":"Pan de molde integral",     "precio":1.80, "stock":40, "categoria":"Panaderia"},
    {"codigo":"P002","nombre":"Pan de molde blanco",       "precio":1.50, "stock":45, "categoria":"Panaderia"},
    {"codigo":"P003","nombre":"Tostadas x20",              "precio":1.30, "stock":35, "categoria":"Panaderia"},
    {"codigo":"P004","nombre":"Croissant x4",              "precio":2.00, "stock":25, "categoria":"Panaderia"},
    {"codigo":"A001","nombre":"Arroz 1kg",                 "precio":0.90, "stock":100,"categoria":"Abarrotes"},
    {"codigo":"A002","nombre":"Arroz 5kg",                 "precio":4.20, "stock":40, "categoria":"Abarrotes"},
    {"codigo":"A003","nombre":"Aceite vegetal 1L",         "precio":2.20, "stock":60, "categoria":"Abarrotes"},
    {"codigo":"A004","nombre":"Azucar blanca 1kg",         "precio":0.75, "stock":90, "categoria":"Abarrotes"},
    {"codigo":"A005","nombre":"Sal 500g",                  "precio":0.35, "stock":80, "categoria":"Abarrotes"},
    {"codigo":"A006","nombre":"Atun en lata 180g",         "precio":1.40, "stock":70, "categoria":"Abarrotes"},
    {"codigo":"A007","nombre":"Sardinas en lata 125g",     "precio":1.10, "stock":65, "categoria":"Abarrotes"},
    {"codigo":"A008","nombre":"Pasta espagueti 500g",      "precio":0.85, "stock":75, "categoria":"Abarrotes"},
    {"codigo":"A009","nombre":"Salsa de tomate 500g",      "precio":1.30, "stock":55, "categoria":"Abarrotes"},
    {"codigo":"A010","nombre":"Mayonesa 200g",             "precio":1.00, "stock":60, "categoria":"Abarrotes"},
    {"codigo":"C001","nombre":"Jabon de manos 250ml",      "precio":1.20, "stock":60, "categoria":"Limpieza"},
    {"codigo":"C002","nombre":"Shampoo 400ml",             "precio":3.50, "stock":35, "categoria":"Limpieza"},
    {"codigo":"C003","nombre":"Papel higienico x4",        "precio":1.80, "stock":55, "categoria":"Limpieza"},
    {"codigo":"C004","nombre":"Papel higienico x12",       "precio":4.80, "stock":30, "categoria":"Limpieza"},
    {"codigo":"C005","nombre":"Detergente en polvo 500g",  "precio":1.60, "stock":45, "categoria":"Limpieza"},
    {"codigo":"C006","nombre":"Suavizante ropa 500ml",     "precio":2.00, "stock":40, "categoria":"Limpieza"},
    {"codigo":"C007","nombre":"Lavavajillas 500ml",        "precio":1.50, "stock":50, "categoria":"Limpieza"},
    {"codigo":"G001","nombre":"Desodorante 150ml",         "precio":2.80, "stock":40, "categoria":"Personal"},
    {"codigo":"G002","nombre":"Pasta dental 100ml",        "precio":1.50, "stock":55, "categoria":"Personal"},
    {"codigo":"G003","nombre":"Cepillo dental",            "precio":1.20, "stock":60, "categoria":"Personal"},
    {"codigo":"G004","nombre":"Afeitadora x2",             "precio":2.50, "stock":30, "categoria":"Personal"},
    {"codigo":"G005","nombre":"Algodon 100g",              "precio":1.00, "stock":45, "categoria":"Personal"},
]

inventario = {}

def inicializar_inventario():
    global inventario
    if os.path.exists(ARCHIVO_INVENTARIO):
        with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                inventario[row["codigo"]] = {
                    "codigo": row["codigo"], "nombre": row["nombre"],
                    "precio": float(row["precio"]), "stock": int(row["stock"]),
                    "categoria": row["categoria"],
                }
    else:
        for p in CATALOGO_BASE:
            inventario[p["codigo"]] = dict(p)
        guardar_inventario_csv()

def guardar_inventario_csv():
    with open(ARCHIVO_INVENTARIO, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["codigo","nombre","precio","stock","categoria"])
        for p in inventario.values():
            w.writerow([p["codigo"],p["nombre"],p["precio"],p["stock"],p["categoria"]])

def descontar_stock(carrito):
    for item in carrito:
        inventario[item["codigo"]]["stock"] -= item["cantidad"]
    guardar_inventario_csv()

def inicializar_csv_ventas():
    if not os.path.exists(ARCHIVO_TRANSACCIONES):
        with open(ARCHIVO_TRANSACCIONES, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["id_transaccion","fecha","hora","cajero",
                                    "subtotal","iva","total","metodo_pago","estado"])
    if not os.path.exists(ARCHIVO_DETALLES):
        with open(ARCHIVO_DETALLES, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["id_transaccion","codigo_producto","nombre_producto",
                                    "precio_unitario","cantidad","subtotal_linea"])

def guardar_transaccion(id_tx, cajero, carrito, metodo):
    ahora    = datetime.now()
    subtotal = sum(i["precio"] * i["cantidad"] for i in carrito)
    iva      = round(subtotal * 0.12, 2)
    total    = round(subtotal + iva, 2)
    with open(ARCHIVO_TRANSACCIONES, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([id_tx, ahora.strftime("%Y-%m-%d"), ahora.strftime("%H:%M:%S"),
                                cajero, round(subtotal,2), iva, total, metodo, "COMPLETADA"])
    with open(ARCHIVO_DETALLES, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        for i in carrito:
            w.writerow([id_tx, i["codigo"], i["nombre"],
                        i["precio"], i["cantidad"], round(i["precio"]*i["cantidad"],2)])
    return subtotal, iva, total

def cargar_transacciones():
    if not os.path.exists(ARCHIVO_TRANSACCIONES):
        return []
    with open(ARCHIVO_TRANSACCIONES, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def siguiente_id():
    txs = cargar_transacciones()
    if not txs:
        return "TX-0001"
    return f"TX-{int(txs[-1]['id_transaccion'].split('-')[1])+1:04d}"


class TPSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TPS — Punto de Venta | QuickShop")
        self.root.geometry("1300x760")
        self.root.configure(bg=BG_OSCURO)
        self.root.resizable(True, True)

        inicializar_inventario()
        inicializar_csv_ventas()

        self.cajero  = "Cajero_01"
        self.carrito = []
        self.var_id  = tk.StringVar(value=siguiente_id())

        self._estilos()
        self._header()
        self._layout()
        self._cargar_catalogo()
        self._cargar_historial()

    def _estilos(self):
        s = ttk.Style()
        s.theme_use("clam")
        s.configure("Treeview", background=BG_CARD, foreground=BLANCO,
                    fieldbackground=BG_CARD, rowheight=26, font=F_CHICA, borderwidth=0)
        s.configure("Treeview.Heading", background=BG_OSCURO, foreground=AZUL,
                    font=("Consolas", 9, "bold"), relief="flat")
        s.map("Treeview", background=[("selected", AZUL_OSC)], foreground=[("selected", BLANCO)])
        s.configure("TCombobox", fieldbackground=BG_CARD, background=BG_CARD,
                    foreground=BLANCO, font=F_CHICA)

    def _header(self):
        bar = tk.Frame(self.root, bg=BG_PANEL, height=56)
        bar.pack(fill="x")
        bar.pack_propagate(False)
        tk.Label(bar, text="🛒  QuickShop — Sistema TPS",
                 font=("Consolas", 14, "bold"), bg=BG_PANEL, fg=AZUL).pack(side="left", padx=18)
        tk.Label(bar, text="v2.0  |  Punto de Venta",
                 font=F_CHICA, bg=BG_PANEL, fg=GRIS).pack(side="left")
        self.lbl_hora = tk.Label(bar, text="", font=F_NORMAL, bg=BG_PANEL, fg=BLANCO)
        self.lbl_hora.pack(side="right", padx=18)
        tk.Label(bar, text=f"👤 {self.cajero}", font=F_NORMAL,
                 bg=BG_PANEL, fg=AMARILLO).pack(side="right", padx=12)
        self._tick()

    def _tick(self):
        self.lbl_hora.config(text="🕐 " + datetime.now().strftime("%d/%m/%Y  %H:%M:%S"))
        self.root.after(1000, self._tick)

    def _layout(self):
        main = tk.Frame(self.root, bg=BG_OSCURO)
        main.pack(fill="both", expand=True, padx=10, pady=(4,10))
        main.columnconfigure(0, weight=3)
        main.columnconfigure(1, weight=3)
        main.columnconfigure(2, weight=2)
        main.rowconfigure(0, weight=1)
        self._panel_catalogo(main)
        self._panel_venta(main)
        self._panel_historial(main)

    # ── PANEL CATÁLOGO ────────────────────
    def _panel_catalogo(self, parent):
        f = tk.Frame(parent, bg=BG_PANEL)
        f.grid(row=0, column=0, padx=(0,5), pady=2, sticky="nsew")

        tk.Label(f, text="📦  CATÁLOGO & STOCK",
                 font=F_TITULO, bg=BG_PANEL, fg=AZUL).pack(anchor="w", padx=12, pady=(10,4))

        fil = tk.Frame(f, bg=BG_PANEL)
        fil.pack(fill="x", padx=10, pady=(0,4))
        tk.Label(fil, text="🔍", font=F_NORMAL, bg=BG_PANEL, fg=GRIS).pack(side="left")
        self.var_busq = tk.StringVar()
        self.var_busq.trace("w", lambda *a: self._cargar_catalogo())
        tk.Entry(fil, textvariable=self.var_busq, font=F_NORMAL,
                 bg=BG_CARD, fg=BLANCO, insertbackground=BLANCO,
                 relief="flat", bd=4).pack(side="left", fill="x", expand=True, padx=4)

        cats = ["Todas"] + sorted({p["categoria"] for p in inventario.values()})
        self.var_cat = tk.StringVar(value="Todas")
        self.var_cat.trace("w", lambda *a: self._cargar_catalogo())
        ttk.Combobox(fil, textvariable=self.var_cat, values=cats,
                     state="readonly", width=10, font=F_CHICA).pack(side="left")

        cols = ("codigo","nombre","precio","stock","cat")
        self.tv_cat = ttk.Treeview(f, columns=cols, show="headings")
        for col, txt, w, anch in [
            ("codigo","Cód.", 60,"center"), ("nombre","Producto",175,"w"),
            ("precio","Precio",65,"center"), ("stock","Stock",55,"center"),
            ("cat","Categ.",80,"center")]:
            self.tv_cat.heading(col, text=txt)
            self.tv_cat.column(col, width=w, anchor=anch)
        self.tv_cat.tag_configure("agotado", foreground=ROJO)
        self.tv_cat.tag_configure("bajo",    foreground=AMARILLO)
        self.tv_cat.tag_configure("normal",  foreground=BLANCO)

        sb = ttk.Scrollbar(f, orient="vertical", command=self.tv_cat.yview)
        self.tv_cat.configure(yscrollcommand=sb.set)
        self.tv_cat.pack(side="left", fill="both", expand=True, padx=(10,0), pady=4)
        sb.pack(side="left", fill="y", pady=4, padx=(0,6))
        self.tv_cat.bind("<Double-1>", lambda e: self._agregar())

        bot = tk.Frame(f, bg=BG_PANEL)
        bot.pack(fill="x", padx=10, pady=8)
        tk.Label(bot, text="Cantidad:", font=F_NORMAL, bg=BG_PANEL, fg=GRIS).pack(side="left")
        self.spin = tk.Spinbox(bot, from_=1, to=99, width=4, font=F_NORMAL,
                               bg=BG_CARD, fg=BLANCO, buttonbackground=BG_CARD, relief="flat")
        self.spin.pack(side="left", padx=6)
        tk.Button(bot, text="➕ Agregar al carrito", font=F_NORMAL,
                  bg=AZUL, fg="white", activebackground=AZUL_OSC, relief="flat",
                  cursor="hand2", command=self._agregar).pack(side="left", fill="x", expand=True)

        ley = tk.Frame(f, bg=BG_PANEL)
        ley.pack(fill="x", padx=12, pady=(0,8))
        for txt, color in [("● Stock OK",VERDE),("● Bajo (<10)",AMARILLO),("● Agotado",ROJO)]:
            tk.Label(ley, text=txt, font=("Consolas",8), bg=BG_PANEL, fg=color).pack(side="left", padx=6)

    # ── PANEL VENTA ───────────────────────
    def _panel_venta(self, parent):
        f = tk.Frame(parent, bg=BG_PANEL)
        f.grid(row=0, column=1, padx=5, pady=2, sticky="nsew")

        enc = tk.Frame(f, bg=BG_CARD)
        enc.pack(fill="x", padx=10, pady=(10,4))
        tk.Label(enc, text="🧾  VENTA EN CURSO", font=F_TITULO,
                 bg=BG_CARD, fg=VERDE).pack(side="left", padx=12, pady=8)
        tk.Label(enc, textvariable=self.var_id,
                 font=("Consolas",11,"bold"), bg=BG_CARD, fg=AMARILLO).pack(side="right", padx=12)

        cols2 = ("nombre","pu","cant","sub")
        self.tv_cart = ttk.Treeview(f, columns=cols2, show="headings")
        for col, txt, w, anch in [
            ("nombre","Producto",200,"w"), ("pu","P.Unit.",75,"center"),
            ("cant","Cant.",55,"center"), ("sub","Subtotal",90,"center")]:
            self.tv_cart.heading(col, text=txt)
            self.tv_cart.column(col, width=w, anchor=anch)
        sb2 = ttk.Scrollbar(f, orient="vertical", command=self.tv_cart.yview)
        self.tv_cart.configure(yscrollcommand=sb2.set)
        self.tv_cart.pack(side="left", fill="both", expand=True, padx=(10,0), pady=4)
        sb2.pack(side="left", fill="y", pady=4, padx=(0,6))

        tk.Button(f, text="🗑️  Quitar producto seleccionado", font=F_CHICA,
                  bg=ROJO, fg="white", activebackground="#c53030", relief="flat",
                  cursor="hand2", command=self._quitar).pack(fill="x", padx=10, pady=(0,4))

        tot = tk.Frame(f, bg=BG_CARD)
        tot.pack(fill="x", padx=10, pady=4)
        self.var_sub   = tk.StringVar(value="$0.00")
        self.var_iva   = tk.StringVar(value="$0.00")
        self.var_total = tk.StringVar(value="$0.00")
        self.var_items = tk.StringVar(value="0 items")

        def fila(lbl, var, color=BLANCO, grande=False):
            r = tk.Frame(tot, bg=BG_CARD)
            r.pack(fill="x", padx=12, pady=2)
            tk.Label(r, text=lbl, font=F_NORMAL, bg=BG_CARD, fg=GRIS).pack(side="left")
            tk.Label(r, textvariable=var,
                     font=("Consolas",13,"bold") if grande else ("Consolas",10,"bold"),
                     bg=BG_CARD, fg=color).pack(side="right")

        fila("Items en carrito:", self.var_items, GRIS)
        fila("Subtotal:", self.var_sub)
        fila("IVA 12%:",  self.var_iva, AMARILLO)
        tk.Frame(tot, bg=BORDE, height=1).pack(fill="x", padx=10, pady=4)
        fila("TOTAL A PAGAR:", self.var_total, VERDE, grande=True)

        mp = tk.Frame(f, bg=BG_PANEL)
        mp.pack(fill="x", padx=10, pady=6)
        tk.Label(mp, text="Metodo de pago:", font=F_NORMAL, bg=BG_PANEL, fg=GRIS).pack(side="left")
        self.var_metodo = tk.StringVar(value="Efectivo")
        for m in ["Efectivo","Tarjeta","Transferencia","QR"]:
            tk.Radiobutton(mp, text=m, variable=self.var_metodo, value=m,
                           font=F_CHICA, bg=BG_PANEL, fg=BLANCO,
                           selectcolor=BG_CARD, activebackground=BG_PANEL).pack(side="left", padx=5)

        acc = tk.Frame(f, bg=BG_PANEL)
        acc.pack(fill="x", padx=10, pady=8)
        tk.Button(acc, text="✅   COBRAR / PROCESAR VENTA",
                  font=("Consolas",12,"bold"), bg=VERDE, fg="white",
                  activebackground=VERDE_OSC, relief="flat", cursor="hand2", height=2,
                  command=self._procesar).pack(fill="x", pady=(0,5))
        tk.Button(acc, text="❌  Cancelar venta", font=F_NORMAL,
                  bg=BG_CARD, fg=ROJO, activebackground=BG_CARD, relief="flat",
                  cursor="hand2", command=self._cancelar).pack(fill="x")

    # ── PANEL HISTORIAL ───────────────────
    def _panel_historial(self, parent):
        f = tk.Frame(parent, bg=BG_PANEL)
        f.grid(row=0, column=2, padx=(5,0), pady=2, sticky="nsew")

        tk.Label(f, text="📋  HISTORIAL DEL DIA",
                 font=F_TITULO, bg=BG_PANEL, fg=AZUL).pack(anchor="w", padx=12, pady=(10,6))

        stats = tk.Frame(f, bg=BG_CARD)
        stats.pack(fill="x", padx=10, pady=(0,6))
        self.var_ntx  = tk.StringVar(value="0")
        self.var_tdia = tk.StringVar(value="$0.00")
        self.var_prom = tk.StringVar(value="$0.00")

        def stat_row(lbl, var, color):
            r = tk.Frame(stats, bg=BG_CARD)
            r.pack(fill="x", padx=10, pady=3)
            tk.Label(r, text=lbl, font=F_CHICA, bg=BG_CARD, fg=GRIS).pack(side="left")
            tk.Label(r, textvariable=var, font=F_TITULO, bg=BG_CARD, fg=color).pack(side="right")

        stat_row("Ventas hoy:",      self.var_ntx,  AMARILLO)
        stat_row("Total recaudado:", self.var_tdia, VERDE)
        stat_row("Ticket promedio:", self.var_prom, AZUL)

        cols3 = ("id","hora","total","metodo","items")
        self.tv_hist = ttk.Treeview(f, columns=cols3, show="headings", height=14)
        for col, txt, w, anch in [
            ("id","ID",72,"center"), ("hora","Hora",60,"center"),
            ("total","Total",65,"center"), ("metodo","Pago",80,"center"),
            ("items","Items",45,"center")]:
            self.tv_hist.heading(col, text=txt)
            self.tv_hist.column(col, width=w, anchor=anch)
        sb3 = ttk.Scrollbar(f, orient="vertical", command=self.tv_hist.yview)
        self.tv_hist.configure(yscrollcommand=sb3.set)
        self.tv_hist.pack(side="left", fill="both", expand=True, padx=(10,0), pady=4)
        sb3.pack(side="left", fill="y", pady=4, padx=(0,6))

        btns = tk.Frame(f, bg=BG_PANEL)
        btns.pack(fill="x", padx=10, pady=4)
        tk.Button(btns, text="🔄 Actualizar historial", font=F_CHICA,
                  bg=BG_CARD, fg=AZUL, activebackground=BG_CARD, relief="flat",
                  cursor="hand2", command=self._cargar_historial).pack(fill="x", pady=(0,4))

        tk.Label(f, text="⚠️  STOCK CRITICO (<10 unid.)",
                 font=F_CHICA, bg=BG_PANEL, fg=AMARILLO).pack(anchor="w", padx=12, pady=(4,2))

        cols4 = ("cod","prod","stock")
        self.tv_crit = ttk.Treeview(f, columns=cols4, show="headings", height=6)
        for col, txt, w in [("cod","Cod",50),("prod","Producto",130),("stock","Stock",50)]:
            self.tv_crit.heading(col, text=txt)
            self.tv_crit.column(col, width=w, anchor="center")
        self.tv_crit.tag_configure("agotado", foreground=ROJO)
        self.tv_crit.tag_configure("bajo",    foreground=AMARILLO)

        sb4 = ttk.Scrollbar(f, orient="vertical", command=self.tv_crit.yview)
        self.tv_crit.configure(yscrollcommand=sb4.set)
        self.tv_crit.pack(side="left", fill="both", expand=True, padx=(10,0), pady=4)
        sb4.pack(side="left", fill="y", pady=4, padx=(0,6))

        self._actualizar_criticos()

    # ── LÓGICA ────────────────────────────
    def _cargar_catalogo(self):
        busq = self.var_busq.get().lower()
        cat  = self.var_cat.get()
        for row in self.tv_cat.get_children():
            self.tv_cat.delete(row)
        for p in sorted(inventario.values(), key=lambda x: x["codigo"]):
            if busq and busq not in p["nombre"].lower() and busq not in p["codigo"].lower():
                continue
            if cat != "Todas" and p["categoria"] != cat:
                continue
            stock = p["stock"]
            tag   = "agotado" if stock == 0 else ("bajo" if stock < 10 else "normal")
            self.tv_cat.insert("", "end", tags=(tag,), values=(
                p["codigo"], p["nombre"], f"${p['precio']:.2f}",
                "AGOTADO" if stock == 0 else stock, p["categoria"]))

    def _agregar(self):
        sel = self.tv_cat.selection()
        if not sel:
            messagebox.showwarning("Aviso", "Selecciona un producto del catalogo.")
            return
        vals   = self.tv_cat.item(sel[0])["values"]
        codigo = vals[0]
        p      = inventario[codigo]
        if p["stock"] == 0:
            messagebox.showerror("Sin stock", f'"{p["nombre"]}" esta agotado.')
            return
        try:
            cantidad = int(self.spin.get())
        except ValueError:
            cantidad = 1
        ya = next((i["cantidad"] for i in self.carrito if i["codigo"] == codigo), 0)
        disponible = p["stock"] - ya
        if cantidad > disponible:
            messagebox.showwarning("Stock insuficiente",
                f'Solo hay {disponible} unidades disponibles de "{p["nombre"]}".')
            return
        for item in self.carrito:
            if item["codigo"] == codigo:
                item["cantidad"] += cantidad
                self._refresh_carrito()
                return
        self.carrito.append({"codigo":codigo,"nombre":p["nombre"],
                              "precio":p["precio"],"cantidad":cantidad})
        self._refresh_carrito()

    def _quitar(self):
        sel = self.tv_cart.selection()
        if not sel:
            return
        self.carrito.pop(self.tv_cart.index(sel[0]))
        self._refresh_carrito()

    def _refresh_carrito(self):
        for row in self.tv_cart.get_children():
            self.tv_cart.delete(row)
        subtotal = 0.0
        for item in self.carrito:
            sub = item["precio"] * item["cantidad"]
            subtotal += sub
            self.tv_cart.insert("", "end", values=(
                item["nombre"], f"${item['precio']:.2f}", item["cantidad"], f"${sub:.2f}"))
        iva   = round(subtotal * 0.12, 2)
        total = round(subtotal + iva, 2)
        n     = sum(i["cantidad"] for i in self.carrito)
        self.var_sub.set(f"${subtotal:.2f}")
        self.var_iva.set(f"${iva:.2f}")
        self.var_total.set(f"${total:.2f}")
        self.var_items.set(f"{n} item{'s' if n!=1 else ''}")

    def _procesar(self):
        if not self.carrito:
            messagebox.showwarning("Carrito vacio", "Agrega productos antes de cobrar.")
            return
        id_tx  = self.var_id.get()
        metodo = self.var_metodo.get()

        # *** DESCONTAR STOCK EN INVENTARIO Y CSV ***
        descontar_stock(self.carrito)

        subtotal, iva, total = guardar_transaccion(id_tx, self.cajero, self.carrito, metodo)

        lineas = "\n".join(
            f"  {i['nombre'][:24]:<24} x{i['cantidad']:>2}  ${i['precio']*i['cantidad']:.2f}"
            for i in self.carrito)
        msg = (
            f"{'='*46}\n"
            f"   RECIBO  -  {id_tx}\n"
            f"{'='*46}\n"
            f"{lineas}\n"
            f"{'-'*46}\n"
            f"  Subtotal : ${subtotal:.2f}\n"
            f"  IVA 12%  : ${iva:.2f}\n"
            f"  TOTAL    : ${total:.2f}\n"
            f"{'-'*46}\n"
            f"  Metodo   : {metodo}    Cajero: {self.cajero}\n"
            f"  Hora     : {datetime.now().strftime('%H:%M:%S')}\n"
            f"{'='*46}\n"
            f"      Gracias por su compra!\n"
        )
        messagebox.showinfo("Venta procesada exitosamente", msg)

        self.carrito = []
        self._refresh_carrito()
        self.var_id.set(siguiente_id())
        self._cargar_catalogo()
        self._cargar_historial()
        self._actualizar_criticos()

    def _cancelar(self):
        if not self.carrito:
            return
        if messagebox.askyesno("Cancelar venta", "Cancelar la venta actual?"):
            self.carrito = []
            self._refresh_carrito()

    def _cargar_historial(self):
        for row in self.tv_hist.get_children():
            self.tv_hist.delete(row)
        txs   = cargar_transacciones()
        hoy   = datetime.now().strftime("%Y-%m-%d")
        total_dia = 0.0
        count = 0
        items_por_tx = {}
        if os.path.exists(ARCHIVO_DETALLES):
            with open(ARCHIVO_DETALLES, "r", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    tid = row["id_transaccion"]
                    items_por_tx[tid] = items_por_tx.get(tid, 0) + int(row["cantidad"])
        for tx in reversed(txs):
            t  = float(tx["total"])
            ni = items_por_tx.get(tx["id_transaccion"], 0)
            self.tv_hist.insert("", "end", values=(
                tx["id_transaccion"], tx["hora"], f"${t:.2f}", tx["metodo_pago"], ni))
            if tx["fecha"] == hoy:
                total_dia += t
                count += 1
        self.var_ntx.set(str(count))
        self.var_tdia.set(f"${total_dia:.2f}")
        self.var_prom.set(f"${(total_dia/count):.2f}" if count else "$0.00")

    def _actualizar_criticos(self):
        for row in self.tv_crit.get_children():
            self.tv_crit.delete(row)
        criticos = sorted([p for p in inventario.values() if p["stock"] < 10],
                          key=lambda x: x["stock"])
        for p in criticos:
            tag = "agotado" if p["stock"] == 0 else "bajo"
            self.tv_crit.insert("", "end", tags=(tag,), values=(
                p["codigo"], p["nombre"][:20],
                "AGOTADO" if p["stock"] == 0 else p["stock"]))


if __name__ == "__main__":
    root = tk.Tk()
    TPSApp(root)
    root.mainloop()