# https://iot.mi.com/new/doc/tools-and-resources/design/spec/description
TRANSLATION_LANGUAGES = {
    'zh': {
        'off': '關機',
        'idle': '閒置',
        'busy': '運作中',
        'pause': '暫停',
        'fault': '錯誤',

        '_globals': {
            'mode': '模式',
            'switch status': '開關',
            'battery level': '電量',
            'target temperature': '目標溫度',
            'temperature': '溫度',
            'relative humidity': '濕度',
            'illumination': '光照度',
            'indicator light': '指示燈',
            'physical control locked': '兒童鎖',
        },

        'fan_level': {
            'auto': '自動',
            # 'low': '低',
            # 'medium': '中',
            # 'middle': '中',
            # 'high': '高',
            'quiet': '靜音',
            'turbo': '超強',
            'level1': '一級',
            'level2': '二級',
            'level3': '三級',
            'level4': '四級',
            'level5': '五級',
            'level6': '六級',
            'level7': '七級',
        },

        'mode': {
            'auto': '自動',
            'basic': '標準',
            'low': '低',
            'medium': '中',
            'high': '高',
            'sleep': '睡眠模式',
            'smart': '智能模式',
            'favorite': '喜愛模式',
        },

        'air_conditioner': {
            'air conditioner': '冷氣機',
        },

        'air_conditioner.mode': {
            'cool': '製冷',
            'dry': '抽濕',
            'fan': '送風',
            'heat': '加熱',
        },

        'air_fresh.mode': {
            'auto': '自動',
            'interval': '間隔',
            'smart': '智能',
            'silent': '靜音',
            'strong': '強力',
            'none': '手動',
            'sleep': '睡眠',
            'favorite': '喜愛',
        },

        'battery': {
            'battery battery level': '電量',
            'battery charging state': '充電狀態',
        },

        'door_state': {
            'open': '開門',
            'close': '關門',
            'close_timeout': '關閉超時',
            'knock': '敲門',
            'breaking': '破門',
            'stuck': '門卡住',
        },

        'fan.mode': {
            'basic': '標準',
            'basic wind': '標準風',
            'straight wind': '直吹風',
            'natural wind': '自然風',
            'energy saving': '節能模式',
            'none': '手動',
            'baby': '嬰兒',
            'smart': '智能',
            'sleep': '睡眠',
            'strong': '強力',
            'circular wind': '循環風',
        },

        'ir_aircondition_control': {
            'ir aircondition control': '红外線冷氣控制',
            'mode for ir': '模式',
            'temperature for ir': '目標溫度',
            'turn on': '打開',
            'turn off': '關閉',
            'fan speed down': '風速-',
            'fan speed up': '風速+',
            'temperature down': '溫度-',
            'temperature up': '溫度+',
        },
        'ir_aircondition_control.ir_mode': {
            'auto': '自動',
            'cool': '製冷',
            'dry': '抽濕',
            'fan': '風扇',
            'heat': '加熱',
        },

        'light': {
            'light': '燈光',
        },
        'light.mode': {
            'day': '日光',
            'night': '夜光',
            'color': '彩光',
            'warmth': '溫暖',
            'tv': '電視模式',
            'reading': '閱讀模式',
            'computer': '電腦模式',
            'hospitality': '款待模式',
            'entertainment': '娛樂模式',
            'lighting': '照明',
            'night light': '夜燈',
        },

        'lock_method': {
            'bluetooth': '藍牙',
            'password': '密碼',
            'biological': '生物認證',
            'key': '鎖匙',
            'turntable': '轉盤',
            'nfc': 'NFC',
            'one-time password': '一次性密碼',
            'two-step verification': '雙重認證',
            'coercion': '強制',
            'homekit': 'Homekit',
            'manual': '手動',
            'automatic': '自動',
        },
        'lock_action': {
            'outside_unlock': '門外開鎖',
            'lock': '鎖上',
            'anti_lock_on': '反鎖定開啟',
            'anti_lock_off': '反鎖定關閉',
            'inside_unlock': '門內開鎖',
            'lock_inside': '門內上鎖',
            'child_lock_on': '開啟兒童鎖',
            'child_lock_off': '關閉兒童鎖',
            'lock_outside': '門外上鎖',
        },

        'magnet_sensor': {
            'magnet sensor': '門窗感應器',
        },

        'motion_sensor': {
            'motion sensor': '動作偵測',
            'motion sensor illumination': '光照度',
        },

        'physical_control_locked': {
            'physical control locked': '物理控制鎖定',
        },

        'play_control': {
            'play control': '播放控制',
            'keycodes': '鍵碼',
        },

        'power_consumption': {
            'power consumption': '耗電量',
            'power consumption electric power': '功率',
            'power consumption electric current': '電流',
            'power consumption electric voltage': '電壓',
        },

        'ptc_bath_heater': {
            'ptc bath heater': '浴霸',
        },
        'ptc_bath_heater.mode': {
            'fan': '吹風',
            'heat': '暖風',
            'ventilate': '通風',
            'dry': '抽濕',
            'defog': '除霧',
            'quick heat': '快速加熱',
            'quick defog': '快速除霧',
        },

        'speaker': {
            'speaker': '喇叭',
            'speaker volume': '音量',
        },

        'sweep.suction_state': {
            'medium': '中',
            'silent': '靜音',
            'slient': '靜音',
            'standard': '標準',
            'turbo': '超強',
        },

        'television': {
            'input control': '輸入控制',
            'tv input control': '輸入控制',
        },

        'temperature_humidity_sensor': {
            'temperature humidity sensor temperature': '溫度',
            'temperature humidity sensor relative humidity': '濕度',
            'temperature humidity sensor atmospheric pressure': '氣壓',
        },

        'vacuum': {
            'robot cleaner': '掃地機械人',
            'robot cleaner status': '掃地機械人狀態',
        },

        'vacuum.mode': {
            'basic': '正常',
            'silent': '安靜',
            'standard': '標準',
            'strong': '強力',
            'turbo': '超強',
            'full speed': '全速',
        },

        'washer': {
            'drying level': '乾燥程度',
            'rinsh times': '沖洗時間',
            'spin speed': '轉速',
            'target water level': '水位',
        },
        'washer.mode': {
            'baby care': '嬰兒護理',
            'boiling': '高溫清洗',
            'color protection': '護色清洗',
            'cotton': '棉麻洗滌',
            'daily wash': '日常清洗',
            'delicate wash': '輕柔清洗',
            'down coat': '羽绒服',
            'drum clean': '自動清洗滾筒',
            'drum dry': '滾筒乾燥',
            'dry air wash': '空載清洗',
            'dry timing': '定時烘乾',
            'dry': '烘乾',
            'gold wash': '黄金清洗',
            'heavy wash': '強力清洗',
            'intensive': '精细清洗',
            'jacket': '外套',
            'jeans': '牛仔褲',
            'mite removal': '除蟎',
            'quick wash dry': '快洗烘乾',
            'quick wash': '快洗',
            'rinse spin': '漂洗旋轉',
            'rinse': '沖洗',
            'shirt': '恤衫',
            'silk': '絲綢',
            'soak wash': '浸泡清洗',
            'sock': '襪子',
            'spin': '脱水',
            'sportswear': '運動衫',
            'super quick': '超快清洗',
            'synthetic': '合成物料',
            'towel': '毛巾',
            'underwear': '内衣',
            'user define': '自訂',
            'wash dry': '洗+烘乾',
            'wool': '羊毛清洗',
        },
        'washer.drying_level': {
            'moist': '微濕',
            'normal': '正常',
            'extra': '特乾',
            'none': '無烘乾',
        },

        'water_heater': {
            'water heater': '熱水爐',
        },
    },

    'el': {
        'off': 'Κλειστή',
        'idle': 'Αδρανής',
        'busy': 'Σε λειτουργία',
        'pause': 'Σε παύση',
        'fault': 'Σφάλμα',

        '_globals': {
            'mode': 'Λειτουργία',
            'switch status': 'Διακόπτες',
            'battery level': 'Επίπεδο μπαταρίας',
            'target temperature': 'Θερμοκρασία-στόχος',
            'temperature': 'Θερμοκρασία',
            'relative humidity': 'Σχετική υγρασία',
            'illumination': 'Φωτισμός',
            'indicator light': 'Ενδεικτική λυχνία',
            'physical control locked': 'Φυσικός έλεγχος κλειδωμένος',
        },

        'fan_level': {
            'auto': 'Αυτόματο',
            # 'low': '低',
            # 'medium': '中',
            # 'middle': '中',
            # 'high': '高',
            'quiet': 'Ήσυχο',
            'turbo': 'Τούρμπο',
            'level1': 'Επίπεδο 1',
            'level2': 'Επίπεδο 2',
            'level3': 'Επίπεδο 3',
            'level4': 'Επίπεδο 4',
            'level5': 'Επίπεδο 5',
            'level6': 'Επίπεδο 6',
            'level7': 'Επίπεδο 7',
        },

        'mode': {
            'auto': 'Αυτόματη',
            'basic': 'Βασική',
            'low': 'Χαμηλή',
            'medium': 'Μεσαία',
            'high': 'Υψηλή',
            'sleep': 'Ύπνος',
            'smart': 'Έξυπνη',
            'favorite': 'Αγαπημένη',
        },

        'air_conditioner': {
            'air conditioner': 'Κλιματισμός',
        },

        'air_conditioner.mode': {
            'cool': 'Ψύξη',
            'dry': 'Αφύγρανση',
            'fan': 'Ανεμιστήρας',
            'heat': 'Θέρμανση',
        },

        'air_fresh.mode': {
            'auto': 'Αυτόματη',
            'interval': 'Διαλείπουσα',
            'smart': 'Έξυπνη',
            'silent': 'Ήσυχη',
            'strong': 'Έντονη',
            'none': 'Καμία',
            'sleep': 'Ύπνος',
            'favorite': 'Αγαπημένη',
        },

        'battery': {
            'battery battery level': 'Επίπεδο μπαταρίας',
            'battery charging state': 'Κατάσταση φόρτισης μπαταρίας',
        },

        'door_state': {
            'open': 'Ανοιχτή',
            'close': 'Κλειστή',
            'close_timeout': 'Χρονικό όριο κλεισίματος',
            'knock': 'Χτύπημα',
            'breaking': 'Σπάσιμο',
            'stuck': 'Κόλλησε',
        },

        'fan.mode': {
            'basic': 'Βασική',
            'basic wind': 'Βασικός άνεμος',
            'straight wind': 'Δυνατός άνεμος',
            'natural wind': 'Φυσικός άνεμος',
            'energy saving': 'Εξοικονόμηση ενέργειας',
            'none': 'Καμία',
            'baby': 'Μωρό',
            'smart': 'Έξυπνη',
            'sleep': 'Ύπνος',
            'strong': 'Δυνατή',
            'circular wind': 'Κυκλικός άνεμος',
        },

        'ir_aircondition_control': {
            'ir aircondition control': 'Υπέρυθρος έλεγχος κλιματισμού',
            'mode for ir': 'Λειτουργία υπέρθυθρων',
            'temperature for ir': 'θερμοκρασία-στόχος',
            'turn on': 'Ενεργοποίηση',
            'turn off': 'Απενεργοποίηση',
            'fan speed down': 'Ταχύτητα ανεμιστήρα -',
            'fan speed up': 'Ταχύτητα ανεμιστήρα +',
            'temperature down': 'Θερμοκρασία -',
            'temperature up': 'Θερμοκρασία +',
        },
        'ir_aircondition_control.ir_mode': {
            'auto': 'Αυτόματο',
            'cool': 'Ψύξη',
            'dry': 'Αφύγρανση',
            'fan': 'Ανεμιστήρας',
            'heat': 'Θέρμανση',
        },

        'light': {
            'light': 'Φωτισμός',
        },
        'light.mode': {
            'day': 'Ημέρα',
            'night': 'Νύχτα',
            'color': 'Χρώμα',
            'warmth': 'Κορεσμός',
            'tv': 'Τηλεόραση',
            'reading': 'Διάβασμα',
            'computer': 'Υπολογιστής',
            'hospitality': 'Φιλοξενία',
            'entertainment': 'Διασκέδαση',
            'lighting': 'Φωτισμός',
            'night light': 'Φωτισμός νυχτός',
        },

        'lock_method': {
            'bluetooth': 'Bluetooth',
            'password': 'Κωδικός πρόσβασης',
            'biological': 'Βιομετρικά',
            'key': 'Κλειδί',
            'turntable': 'Με περιστρεφή',
            'nfc': 'NFC',
            'one-time password': 'Κωδικός πρόσβασης μίας χρήσης',
            'two-step verification': 'Διπλή διαπίστευση',
            'coercion': 'Εξαναγκασμός',
            'homekit': 'Homekit',
            'manual': 'Χειροκίνητη',
            'automatic': 'Αυτόματη',
        },
        'lock_action': {
            'outside_unlock': 'Ξεκλείδωμα εξωτερικής πόρτας',
            'lock': 'Κλείδωμα',
            'anti_lock_on': 'Ενεργοποίηση αντίστροφης κλειδαριάς',
            'anti_lock_off': 'Απενεργοποίηση αντίστροφης κλειδαριάς',
            'inside_unlock': 'Ξεκλείδωμα από μέσα',
            'lock_inside': 'Κλείδωμα μέσα',
            'child_lock_on': 'Ενεργοποίηση παιδικού κλειδώματος',
            'child_lock_off': 'Απενεργοποίηση παιδικού κλειδώματος',
            'lock_outside': 'Κλείδωμα εξωτερικής πόρτας',
        },

        'magnet_sensor': {
            'magnet sensor': 'Αισθητήρες θυρών και παραθύρων',
        },

        'motion_sensor': {
            'motion sensor': 'Ανίχνευση κίνησης',
            'motion sensor illumination': 'Ανίχνευση φωτισμού',
        },

        'physical_control_locked': {
            'physical control locked': 'Κλείδωμα φυσικού ελέγχου',
        },

        'play_control': {
            'play control': 'Έλεγχος αναπαραγωγής',
            'keycodes': 'Κωδικοί κλειδιών',
        },

        'power_consumption': {
            'power consumption': 'Κατανάλωση ενέργειας',
            'power consumption electric power': 'Κατανάλωση ηλεκτρικής ενέργειας',
            'power consumption electric current': 'Κατανάλωση ηλεκτρικού ρεύματος',
            'power consumption electric voltage': 'Κατανάλωση ηλεκτρικής τάσης',
        },

        'ptc_bath_heater': {
            'ptc bath heater': 'Θερμαντήρας μπάνιου ptc',
        },
        'ptc_bath_heater.mode': {
            'fan': 'Ανεμιστήρας',
            'heat': 'Θέρμανση',
            'ventilate': 'Εξαερισμός',
            'dry': 'Αφύγρανση',
            'defog': 'Αποθαμβωτικό',
            'quick heat': 'Γρήγορη ζέστη',
            'quick defog': 'Γρήγορο αποθαμβωτικό',
        },

        'speaker': {
            'speaker': 'Ήχος',
            'speaker volume': 'Ένταση ήχου',
        },

        'sweep.suction_state': {
            'medium': 'Μεσαίο',
            'silent': 'Ήσυχο',
            'slient': 'Ήσυχο',
            'standard': 'Κανονικό',
            'turbo': 'Τούρμπο',
        },

        'sweep.water_state': {
            '低': 'Χαμηλή',
            '中': 'Μεσαία',
            '高': 'Υψηλή',
        },

        'television': {
            'input control': 'Πηγή εισόδου',
            'tv input control': 'Πηγή εισόδου τηλεόρασης',
        },

        'temperature_humidity_sensor': {
            'temperature humidity sensor temperature': 'Θερμοκρασία',
            'temperature humidity sensor relative humidity': 'Υγρασία',
            'temperature humidity sensor atmospheric pressure': 'Ατμοσφαιρική πίεση',
        },

        'vacuum': {
            'robot cleaner': 'Σκούπα δαπέδου',
            'robot cleaner status': 'Κατάσταση σκούπας',
        },

        'vacuum.mode': {
            'basic': 'Βασική',
            'silent': 'Ήσυχη',
            'standard': 'Κανονική',
            'strong': 'Δυνατή',
            'turbo': 'Τούρμπο',
            'full speed': 'Πλήρης ταχύτητα',
        },

        'washer': {
            'drying level': 'Επίπεδο στεγνώματος',
            'rinsh times': 'Αριθμός ξεβγάλματος',
            'spin speed': 'Ταχύτητα περιστροφής',
            'target water level': 'Στάθμη νερού',
        },
        'washer.mode': {
            'baby care': 'Βρεφικό πλύσιμο',
            'boiling': 'Πλύσιμο σε υψηλή θερμοκρασία',
            'color protection': 'Πλύση προστασίας χρώματος',
            'cotton': 'Βαμβάκι και λινό πλύσιμο',
            'daily wash': 'Καθημερινό πλύσιμο',
            'delicate wash': 'Απαλό πλύσιμο',
            'down coat': 'Πουπουλένιο μπουφάν',
            'drum clean': 'Καθαρισμός κάδου',
            'drum dry': 'Στέγνωμα κάδου',
            'dry air wash': 'Πλύσιμο με αέρα',
            'dry timing': 'Χρόνος στεγνώματος',
            'dry': 'Στέγνωμα',
            'gold wash': 'Πλύσιμο χρυσού',
            'heavy wash': 'Ισχυρό πλύσιμο',
            'intensive': 'Εντατικό',
            'jacket': 'Μπουφάν',
            'jeans': 'Τζιν',
            'mite removal': 'Αφαίρεση ακάρεων',
            'quick wash dry': 'Γρήγορο πλύσιμο και στέγνωμα',
            'quick wash': 'Γρήγορο πλύσιμο',
            'rinse spin': 'Λεύκανση και ξέβγαλμα',
            'rinse': 'Ενιαίο ξέβγαλμα',
            'shirt': 'Πουκάμισα',
            'silk': 'Μετάξι',
            'soak wash': 'Πλύσιμο με μούλιασμα',
            'sock': 'Κάλτσες',
            'spin': 'Στύψιμο',
            'sportswear': 'Αθλητικά ρούχα',
            'super quick': 'Σούπερ γρήγορο πλύσιμο',
            'synthetic': 'Συνθετικά',
            'towel': 'Πετσέτες',
            'underwear': 'Εσώρουχα',
            'user define': 'Προσαρμογή',
            'wash dry': 'Πλύσιμο + Στέγνωμα',
            'wool': 'Μαλλί',
        },
        'washer.drying_level': {
            'moist': 'Ελαφρώς υγρό',
            'normal': 'Κανονικό',
            'extra': 'Έξτρα',
            'none': 'Καθόλου',
        },

        'water_heater': {
            'water heater': 'Θερμοσίφωνας νερού',
        },
    },

    'ru': {
        'off': 'Выключенный',
        'idle': 'Бездействующий',
        'busy': 'Занятый',
        'pause': 'Пауза',
        'fault': 'Неисправный',

        '_globals': {
            'mode': 'Режим',
            'switch status': 'Статус переключателя',
            'battery level': 'Уровень заряда батареи',
            'target temperature': 'Целевая температура',
            'temperature': 'Температура',
            'relative humidity': 'Относительная влажность',
            'illumination': 'Освещение',
            'indicator light': 'Световой индикатор',
            'physical control locked': 'Физический контроль заблокирован',
        },

        'fan_level': {
            'auto': 'авто',
            # 'low': 'низкий',
            # 'medium': 'средний',
            # 'middle': 'середина',
            # 'high': 'высокий',
            'quiet': 'тихий',
            'turbo': 'турбо',
            'level1': '1-й уровень',
            'level2': '2-й уровень',
            'level3': '3-й уровень',
            'level4': '4-й уровень',
            'level5': '5-й уровень',
            'level6': '6-й уровень',
            'level7': '7-й уровень',
        },

        'mode': {
            'auto': 'авто',
            'basic': 'базовый',
            'low': 'низкий',
            'medium': 'средний',
            'high': 'высокий',
            'sleep': 'спящий',
            'smart': 'умный',
            'favorite': 'любимый',
        },

        'air_conditioner': {
            'air conditioner': 'кондиционер',
        },

        'air_conditioner.mode': {
            'cool': 'охлаждение',
            'dry': 'осушение',
            'fan': 'вентиляция',
            'heat': 'отопление',
        },

        'air_fresh.mode': {
            'auto': 'авто',
            'interval': 'интервал',
            'smart': 'умный',
            'silent': 'тихий',
            'strong': 'сильный',
            'none': 'никакой',
            'sleep': 'спящий',
            'favorite': 'любимый',
        },

        'battery': {
            'battery battery level': 'уровень заряда батареи',
            'battery charging state': 'состояние зарядки аккумулятора',
        },

        'door_state': {
            'open': 'открыта',
            'close': 'закрыта',
            'close_timeout': 'тайм-аут_закрытия',
            'knock': 'стук',
            'breaking': 'нарушение',
            'stuck': 'застрявший',
        },

        'fan.mode': {
            'basic': 'базовый',
            'basic wind': 'базовая скорость вентилятора',
            'straight wind': 'ровная скорость вентилятора',
            'natural wind': 'естественная скорость вентилятора',
            'energy saving': 'сохранение энергии',
            'none': 'никакой',
            'baby': 'ребенок',
            'smart': 'умный',
            'sleep': 'спящий',
            'strong': 'сильный',
            'circular wind': 'круговая скорость вентилятора',
        },

        'ir_aircondition_control': {
            'ir aircondition control': 'управление кондиционером',
            'mode for ir': 'режим',
            'temperature for ir': 'температура',
            'turn on': 'включить',
            'turn off': 'выключить',
            'fan speed down': 'понизить скорость вентилятора-',
            'fan speed up': 'увеличить скорость вентилятора+',
            'temperature down': 'понизить температуру-',
            'temperature up': 'увеличить температуру+',
        },
        'ir_aircondition_control.ir_mode': {
            'auto': 'авто',
            'cool': 'охлаждение',
            'dry': 'осушение',
            'fan': 'вентиляция',
            'heat': 'отопление',
        },

        'light': {
            'light': 'свет',
        },
        'light.mode': {
            'day': 'день',
            'night': 'ночь',
            'color': 'цвет',
            'warmth': 'теплый',
            'tv': 'телевизор',
            'reading': 'чтение',
            'computer': 'компьютер',
            'hospitality': 'гостеприимство',
            'entertainment': 'развлечения',
            'lighting': 'освещение',
            'night light': 'ночной свет',
        },

        'lock_method': {
            'bluetooth': 'bluetooth',
            'password': 'пароль',
            'biological': 'биологический',
            'key': 'ключ',
            'turntable': 'поворотный круг',
            'nfc': 'NFC',
            'one-time password': 'одноразовый пароль',
            'two-step verification': 'двухэтапная проверка',
            'coercion': 'сдерживание',
            'homekit': 'Homekit',
            'manual': 'руководство',
            'automatic': 'автоматический',
        },
        'lock_action': {
            'outside_unlock': 'внешняя разблокировка',
            'lock': 'замок',
            'anti_lock_on': 'антиблокировка включена',
            'anti_lock_off': 'антиблокировочное отключение',
            'inside_unlock': 'разблокировать внутри',
            'lock_inside': 'замок внутри',
            'child_lock_on': 'блокировка от детей включена',
            'child_lock_off': 'блокировка от детей выключена',
            'lock_outside': 'замок снаружи',
        },

        'magnet_sensor': {
            'magnet sensor': 'магнитный датчик',
        },

        'motion_sensor': {
            'motion sensor': 'датчик движения',
            'motion sensor illumination': 'подсветка датчика движения',
        },

        'physical_control_locked': {
            'physical control locked': 'Физический контроль заблокирован',
        },

        'play_control': {
            'play control': 'контроль',
            'keycodes': 'коды клавиш',
        },

        'power_consumption': {
            'power consumption': 'потребляемая мощность',
            'power consumption electric power': 'потребляемая электрическая мощность',
            'power consumption electric current': 'потребляемый электрический ток',
            'power consumption electric voltage': 'потребляемое электрическое напряжение',
        },

        'ptc_bath_heater': {
            'ptc bath heater': 'нагреватель для ванны',
        },
        'ptc_bath_heater.mode': {
            'fan': 'вентилятор',
            'heat': 'отопление',
            'ventilate': 'вентиляция',
            'dry': 'осушение',
            'defog': 'устранение запотевания',
            'quick heat': 'быстрый нагрев',
            'quick defog': 'быстрое устранение запотевания',
        },

        'speaker': {
            'speaker': 'динамик',
            'speaker volume': 'громкость динамика',
        },

        'television': {
            'input control': 'управление входом',
            'tv input control': 'управление входом телевизора',
        },

        'temperature_humidity_sensor': {
            'temperature humidity sensor temperature': 'температура датчик влажности',
            'temperature humidity sensor relative humidity': 'относительная влажность датчика температуры',
            'temperature humidity sensor atmospheric pressure': 'атмосферное давление датчика температуры влажности',
        },

        'vacuum': {
            'robot cleaner': 'робот-пылесос',
            'robot cleaner status': 'статус робота-пылесоса',
            'robot cleaner mode': 'режим уборки',
            'robot cleaner sweep type': 'тип уборки',
        },
        'alarm': {
            'alarm': 'Подать сигнал',
            'alarm volume': 'Громкость',
        },
        'vacuum.status': {
            'sleep': 'Сон',
            'idle': 'Ожидание',
            'paused': 'На паузе',
            'go charging': 'Едет на зарядку',
            'charging': 'Заряжается',
            'sweeping': 'Сухая уборка',
            'sweeping and mopping': 'Сухая и влажная уборки', 
            'mopping': 'Влажная уборка',
            'upgrading': 'Обновление',
        },
        'vacuum.mode': {
            'basic': 'базовый',
            'silent': 'тихий',
            'standard': 'стандартный',
            'strong': 'сильный',
            'turbo': 'турбо',
            'full speed': 'максимальная скорость',
            'sweep': 'Сухая',
            'sweep and mop': 'Сухая и влажная',
            'mop': 'Влажная',
        },
        'vacuum.sweep_type': {
            'Global': 'Глобальная',
            'Mop': 'Влажная',
            'Edge': 'Периметр',
            'Area': 'Зона',
            'Point': 'Точка',
            'Remote': 'Удаленное управление',
            'Explore': 'Обследование',
            'Room': 'Комната',
            'Floor': 'Этаж',
        },
        'sweep': {
            'sweep door-state': 'конейнер',
            'sweep cloth-state': 'тряпка',
            'sweep hypa-life': 'ресурс фильтра',
            'sweep mop-life': 'ресурс тряпки',
            'sweep main-brush-life': 'ресурс основной щетки',
            'sweep side-brush-life': 'ресурс боковой щетки',
            'sweep repeat-state': 'двойная уборка',
            'sweep water_state': 'смачивание тряпки',
            'sweep cleaning_area': 'площадь уборки',
            'sweep cleaning_time': 'время уборки',
            'sweep pet-recognize': 'распознование животных',
            'sweep mop-route': 'тип влажной уборки',
            'sweep ai_recognize': 'распознование AI',
            'sweep dirt-recognize': 'распознование грязи',            
        },
        'sweep.water_state': {
            '低': 'Низкое',
            '中': 'Среднее',
            '高': 'Высокое',
        },
        'sweep.mop_route': {
            'Y 字': 'Улучшенная',
            '弓字': 'Обычная',
        },
        'sweep.suction_state': {
            'medium': 'средний',
            '標準': 'Средняя',
            'silent': 'тихий',
            'slient': 'тихий',
            '關': 'Тихая',
            'standard': 'стандартный',
            '節能': 'Стандартная',
            'turbo': 'турбо',
            '超強': 'Турбо',
        },
        'sweep.door_state': {
            '無': 'Извлечен',
            '塵盒': 'Для мусора',
            '水箱': 'Для воды',
            '二合一水箱': 'Совмещенный',
        },
        'sweep.cloth_state': {
            '未安裝': 'отсутсвует',
            '已安裝': 'установлена',
        },
        'clean.mode': {
            '安靚': 'Тихий',
            '標準': 'Стандартный',
            '中': 'Средний',
            '超強': 'Турбо',
        },

        'washer': {
            'drying level': 'уровень сушки',
            'rinsh times': 'время полоскания',
            'spin speed': 'скорость отжима',
            'target water level': 'целевой уровень воды',
        },
        'washer.mode': {
            'baby care': 'забота о ребенке',
            'boiling': 'кипячение',
            'color protection': 'защита цвета',
            'cotton': 'хлопок',
            'daily wash': 'ежедневная стирка',
            'delicate wash': 'деликатная стирка',
            'down coat': 'пуховик',
            'drum clean': 'очистка барабана',
            'drum dry': 'сушка в барабане',
            'dry air wash': 'сушка воздухом',
            'dry timing': 'время сушки',
            'dry': 'сушить',
            'gold wash': 'золотая стирка',
            'heavy wash': 'крупная стирка',
            'intensive': 'интенсивный',
            'jacket': 'куртка',
            'jeans': 'джинсы',
            'mite removal': 'удаление клеща',
            'quick wash dry': 'быстрая сухая стирка',
            'quick wash': 'быстрая стирка',
            'rinse spin': 'режим полоскания',
            'rinse': 'полоскать',
            'shirt': 'рубашка',
            'silk': 'шелк',
            'soak wash': 'замочить',
            'sock': 'носок',
            'spin': 'вращение',
            'sportswear': 'спортивная одежда',
            'super quick': 'супер быстро',
            'synthetic': 'синтетический',
            'towel': 'полотенце',
            'underwear': 'нижнее белье',
            'user define': 'определяемые пользователем',
            'wash dry': 'вымыть и высушить',
            'wool': 'шерсть',
        },
        'washer.drying_level': {
            'moist': 'влажный',
            'normal': 'обычный',
            'extra': 'дополнительный',
            'none': 'ничего',
        },

        'water_heater': {
            'water heater': 'водонагреватель',
        },
    },

    'en': {
        'clean.mode': {
            '安靜': 'Silent',
            '標準': 'Standard',
            '中': 'Medium',
            '超強': 'Turbo',
        },
        'sweep.suction_state': {
            'slient': 'Silent',
            '關': 'Silent',
            '節能': 'Standard',
            '標準': 'Medium',
            '超強': 'Turbo',
        },
        'sweep.water_state': {
            '低': 'Low',
            '中': 'Medium',
            '高': 'High',
        },
        'viomi_vacuum': {
            '1級': 'Level 1',
            '2級': 'Level 2',
            '3級': 'Level 3',
            'dust-collection': 'Dust Collection',
            'door-state': 'Dust Bin State',
            '出水量大小': 'Mop Water Volume',
            '邊刷剩餘壽命百分比': 'Side Brush Life',
            '邊刷剩餘壽命小時': 'Side Brush Hours',
            '主刷剩餘壽命百分比': 'Main Brush Life',
            '主刷剩餘壽命小時': 'Main Brush Hours',
            '拖布剩餘壽命百分比': 'Mop Life',
            '拖布剩餘壽命小時': 'Mop Hours',
            'hypa_hours': 'Dust Box Filter Hours',
            'hypa_life': 'Dust Box Filter Life',
            '清掃使用時間，單位秒': 'Cleaning time',
            '清掃總面積，單位m2': 'Cleaned area',
            '清掃開始時間，時間戳，單位秒': 'Cleaning start time, timestamp, in seconds',
            'Y字形': 'Y-shaped',
            '弓字形': 'S-shaped',
        },
    },

    'pl': {
        'off': 'Wyłączony',
        'idle': 'Pracuje',
        'busy': 'Zajęty',
        'pause': 'Wstrzymany',
        'fault': 'Błąd',

        '_globals': {
            'mode': 'Tryb',
            'switch status': 'Status przełącznika',
            'battery level': 'Poziom baterii',
            'target temperature': 'Temperatura docelowa',
            'temperature': 'Temperatura',
            'relative humidity': 'Wilgotność',
            'illumination': 'Jasność',
            'indicator light': 'Wskaźnik światła',
            'physical control locked': 'Blokada fizyczna',
        },

        'fan_level': {
            'auto': 'auto',
            # 'low': 'niski',
            # 'medium': 'średni',
            # 'middle': 'średnio wysoki',
            # 'high': 'wysoki',
            'quiet': 'cichy',
            'turbo': 'turbo',
            'level1': 'poziom1',
            'level2': 'poziom2',
            'level3': 'poziom3',
            'level4': 'poziom4',
            'level5': 'poziom5',
            'level6': 'poziom6',
            'level7': 'poziom7',
        },

        'mode': {
            'auto': 'auto',
            'basic': 'podstawowy',
            'low': 'niski',
            'medium': 'średni',
            'high': 'wysoki',
            'sleep': 'nocny',
            'smart': 'smart',
            'favorite': 'ulubiony',
        },

        'air_conditioner': {
            'air conditioner': 'klimatyzacja',
        },

        'air_conditioner.mode': {
            'cool': 'chłodzenie',
            'dry': 'suszenie',
            'fan': 'wiatrak',
            'heat': 'grzanie',
        },

        'air_fresh.mode': {
            'auto': 'auto',
            'interval': 'przerywany',
            'smart': 'smart',
            'silent': 'cichy',
            'strong': 'mocny',
            'none': 'brak',
            'sleep': 'nocny',
            'favorite': 'ulubiony',
        },

        'battery': {
            'battery battery level': 'poziom baterii',
            'battery charging state': 'status baterii',
        },

        'fan.mode': {
            'basic': 'podstawowy',
            'basic wind': 'podstawowy wiatr',
            'straight wind': 'prosty wiatr',
            'natural wind': 'naturalny wiatr',
            'energy saving': 'oszczędzanie energii',
            'none': 'brak',
            'baby': 'dzieciecy',
            'smart': 'smart',
            'sleep': 'nocny',
            'strong': 'mocny',
            'circular wind': 'cyrkulacja wiatrem',
        },

        'ir_aircondition_control': {
            'ir aircondition control': 'pilot podczerwieni',
            'mode for ir': 'tryb dla pilota',
            'temperature for ir': 'temperatura dla pilota',
            'turn on': 'Włącz',
            'turn off': 'Wyłącz',
            'fan speed down': 'zmniejsz prędkość',
            'fan speed up': 'zwiększ prędkość',
            'temperature down': 'zmniejsz temperaturę',
            'temperature up': 'zwiększ temperaturę',
        },
        'ir_aircondition_control.ir_mode': {
            'auto': 'auto',
            'cool': 'chłodzenie',
            'dry': 'osuszanie',
            'fan': 'wiatrak',
            'heat': 'ogrzewanie',
        },

        'light': {
            'light': 'światło',
        },
        'light.mode': {
            'day': 'dzienne',
            'night': 'nocne',
            'color': 'kolor',
            'warmth': 'ciepło',
            'tv': 'telewizyjny',
            'reading': 'czytanie',
            'computer': 'komputerowy',
            'hospitality': 'gościnny',
            'entertainment': 'imprezowy',
            'lighting': 'oświetlający',
            'night light': 'nocny',
        },

        'magnet_sensor': {
            'magnet sensor': 'czujnik magnetyczny',
        },

        'motion_sensor': {
            'motion sensor': 'czujnik ruchu',
            'motion sensor illumination': 'czujnik światła',
        },

        'physical_control_locked': {
            'physical control locked': 'blokada fizyczna',
        },

        'play_control': {
            'play control': 'sterowanie odtwarzaniem',
            'keycodes': 'kody klawiszy',
        },

        'power_consumption': {
            'power consumption': 'pobór energii',
            'power consumption electric power': 'moc',
            'power consumption electric current': 'prąd',
            'power consumption electric voltage': 'napięcie',
        },

        'ptc_bath_heater': {
            'ptc bath heater': 'grzejnik łazienkowy',
        },
        'ptc_bath_heater.mode': {
            'fan': 'wiatrak',
            'heat': 'ogrzewanie',
            'ventilate': 'wentylacja',
            'dry': 'osuszanie',
            'defog': 'odparowanie',
            'quick heat': 'szybkie grzanie',
            'quick defog': 'szybkie odparowanie',
        },

        'speaker': {
            'speaker': 'głośnik',
            'speaker volume': 'głośność',
        },

        'television': {
            'input control': 'wejścia',
            'tv input control': 'TV wejścia',
        },

        'temperature_humidity_sensor': {
            'temperature humidity sensor temperature': 'temperatura',
            'temperature humidity sensor relative humidity': 'wilgotność',
            'temperature humidity sensor atmospheric pressure': 'ciśnienie',
        },

        'vacuum': {
            'robot cleaner': 'Odkurzacz',
            'robot cleaner status': 'stan',
        },

        'vacuum.mode': {
            'basic': 'podstawowy',
            'silent': 'cichy',
            'standard': 'standardowy',
            'strong': 'mocny',
            'turbo': 'turbo',
            'full speed': 'maksymalny',
        },

        'washer': {
            'drying level': 'poziom suszenia',
            'rinsh times': 'czas płukania',
            'spin speed': 'prędkość wirowania',
            'target water level': 'poziom wody',
        },
        'washer.mode': {
            'baby care': 'dziecięcy',
            'boiling': 'wyparzanie',
            'color protection': 'ochrona kolorów',
            'cotton': 'bawełna',
            'daily wash': 'codzienne',
            'delicate wash': 'delikatne',
            'down coat': 'kurtka puchowa',
            'drum clean': 'czyszczenie bębna ',
            'drum dry': 'suszenie bębna',
            'dry air wash': 'pranie suchym powietrzem',
            'dry timing': 'suszenie czasowe',
            'dry': 'suszenie',
            'gold wash': 'gold wash',
            'heavy wash': 'ciężkie pranie',
            'intensive': 'intensywny',
            'jacket': 'kurtka',
            'jeans': 'jeans',
            'mite removal': 'usuwanie roztoczy',
            'quick wash dry': 'szybkie pranie parowe',
            'quick wash': 'szybkie pranie',
            'rinse spin': 'wirowanie z płukaniem',
            'rinse': 'płukanie',
            'shirt': 'koszula',
            'silk': 'jedwab',
            'soak wash': 'namaczanie',
            'sock': 'skarpetki',
            'spin': 'wirowanie',
            'sportswear': 'odzież sportowa',
            'super quick': 'super szybkie',
            'synthetic': 'syntetyczne',
            'towel': 'ręczniki',
            'underwear': 'bielizna',
            'user define': 'ustawienia własne',
            'wash dry': 'pranie parowe',
            'wool': 'wełna',
        },
        'washer.drying_level': {
            'moist': 'wilgotny',
            'normal': 'nirmalny',
            'extra': 'ekstra',
            'none': 'brak',
        },

        'water_heater': {
            'water heater': 'podgrzewacz wody',
        },
    },
    'hu': {
        'off': 'Kikapcsolva',
        'idle': 'Tétlen',
        'busy': 'Elfoglalt',
        'pause': 'Szünetel',
        'fault': 'Hibás',

        '_globals': {
            'mode': 'Mód',
            'switch status': 'Kapcsoló állapota',
            'battery level': 'Akkumulátor szintje',
            'target temperature': 'Célhőmérséklet',
            'temperature': 'Hőmérséklet',
            'relative humidity': 'Relatív páratartalom',
            'illumination': 'Megvilágítás',
            'indicator light': 'Jelzőfény',
            'physical control locked': 'Fizikai vezérlés zárolva',
        },

        'fan_level': {
            'auto': 'auto',
            # 'low': 'alacsony',
            # 'medium': 'közepes',
            # 'middle': 'közepes',
            # 'high': 'magas',
            'quiet': 'halk',
            'turbo': 'turbó',
            'level1': 'szint1',
            'level2': 'szint2',
            'level3': 'szint3',
            'level4': 'szint4',
            'level5': 'szint5',
            'level6': 'szint6',
            'level7': 'szint7',
        },

        'mode': {
            'auto': 'auto',
            'basic': 'alap',
            'low': 'alacsony',
            'medium': 'közepes',
            'high': 'magas',
            'sleep': 'alvó',
            'smart': 'okos',
            'favorite': 'kedvenc',
        },

        'air_conditioner': {
            'air conditioner': 'légkondícionáló',
        },

        'air_conditioner.mode': {
            'cool': 'hűtés',
            'dry': 'szárítás',
            'fan': 'ventilátor',
            'heat': 'fűtés',
        },

        'air_fresh.mode': {
            'auto': 'auto',
            'interval': 'időszakos',
            'smart': 'okos',
            'silent': 'csendes',
            'strong': 'erős',
            'none': 'egyik sem',
            'sleep': 'alvó',
            'favorite': 'kedvenc',
        },

        'battery': {
            'battery battery level': 'akkumulátorszint',
            'battery charging state': 'akkumulátor töltés állapota',
        },

        'fan.mode': {
            'basic': 'alap',
            'basic wind': 'alap fújás',
            'straight wind': 'egyenes fújás',
            'natural wind': 'természetes szél',
            'energy saving': 'energiatakarékos',
            'none': 'brak',
            'baby': 'bébi',
            'smart': 'okos',
            'sleep': 'alvó',
            'strong': 'erős',
            'circular wind': 'körkörös fújás',
        },

        'ir_aircondition_control': {
            'ir aircondition control': 'infravörös légkondícionáló vezérlés',
            'mode for ir': 'infravörös módja',
            'temperature for ir': 'infravörös hőmérséklet',
            'turn on': 'bekapcsolás',
            'turn off': 'kikapcsolás',
            'fan speed down': 'ventilátor sebesség fel',
            'fan speed up': 'ventilátor sebesség le',
            'temperature down': 'hőmérséklet fel',
            'temperature up': 'hőmérséklet le',
        },
        'ir_aircondition_control.ir_mode': {
            'auto': 'auto',
            'cool': 'hűtés',
            'dry': 'szárítás',
            'fan': 'ventilátor',
            'heat': 'fűtés',
        },

        'light': {
            'light': 'fény',
        },
        'light.mode': {
            'day': 'nappal',
            'night': 'éjszaka',
            'color': 'szín',
            'warmth': 'meleg',
            'tv': 'televízió',
            'reading': 'olvasás',
            'computer': 'számítógép',
            'hospitality': 'vendégszeretet',
            'entertainment': 'szórakozás',
            'lighting': 'villámlás',
            'night light': 'éjjelifény',
        },

        'magnet_sensor': {
            'magnet sensor': 'mégneses érzékelő',
        },

        'motion_sensor': {
            'motion sensor': 'mozgásérzékelő',
            'motion sensor illumination': 'mozgásérzékelő fényerősség',
        },

        'physical_control_locked': {
            'physical control locked': 'fizikai vezérlés zárolva',
        },

        'play_control': {
            'play control': 'lejátszásvezérlés',
            'keycodes': 'kulcskódok',
        },

        'power_consumption': {
            'power consumption': 'enegriafogyasztás',
            'power consumption electric power': 'teljesítmény',
            'power consumption electric current': 'áramerősség',
            'power consumption electric voltage': 'feszültség',
        },

        'ptc_bath_heater': {
            'ptc bath heater': 'fürdőszobai hősugárzó',
        },
        'ptc_bath_heater.mode': {
            'fan': 'ventilátor',
            'heat': 'fűtés',
            'ventilate': 'szellőzés',
            'dry': 'szárítás',
            'defog': 'párátlanítás',
            'quick heat': 'gyors fűtés',
            'quick defog': 'gyors párátlanítás',
        },

        'speaker': {
            'speaker': 'hangszóró',
            'speaker volume': 'hangszóró hangereje',
        },

        'television': {
            'input control': 'bevitel vezérlés',
            'tv input control': 'TV bevitel vezérlés',
        },

        'temperature_humidity_sensor': {
            'temperature humidity sensor temperature': 'hőmérséklet',
            'temperature humidity sensor relative humidity': 'páratartalom',
            'temperature humidity sensor atmospheric pressure': 'légnyomás',
        },

        'vacuum': {
            'robot cleaner': 'robotporszívó',
            'robot cleaner status': 'állapot',
        },

        'vacuum.mode': {
            'basic': 'alap',
            'silent': 'csendes',
            'standard': 'alapértelmezett',
            'strong': 'erős',
            'turbo': 'turbó',
            'full speed': 'maximális sebesség',
        },

        'washer': {
            'drying level': 'szárítási szint',
            'rinsh times': 'öblítések száma',
            'spin speed': 'centrifuga sebesség',
            'target water level': 'cél víz szint',
        },
        'washer.mode': {
            'baby care': 'babaápolás',
            'boiling': 'kifőzés',
            'color protection': 'színvédelem',
            'cotton': 'gyapot',
            'daily wash': 'napi mosás',
            'delicate wash': 'finom mosás',
            'down coat': 'pehelykabát',
            'drum clean': 'dobtisztítás',
            'drum dry': 'szekrényszáraz',
            'dry air wash': 'száraz levegős mosás',
            'dry timing': 'szárítási idő',
            'dry': 'szárítás',
            'gold wash': 'gold wash',
            'heavy wash': 'nehéz szennyeződés',
            'intensive': 'intenzív',
            'jacket': 'dzseki',
            'jeans': 'farmer',
            'mite removal': 'atka eltávolító',
            'quick wash dry': 'gyors mosás és szárítás',
            'quick wash': 'gyors mosás',
            'rinse spin': 'centrifugálás öblítéssel',
            'rinse': 'öblítés',
            'shirt': 'póló',
            'silk': 'selyem',
            'soak wash': 'áztatásos mosás',
            'sock': 'zokni',
            'spin': 'kötött',
            'sportswear': 'sportruházat',
            'super quick': 'szupergyors',
            'synthetic': 'szintetikus',
            'towel': 'törölköző',
            'underwear': 'fehérnamű',
            'user define': 'egyéni beállítás',
            'wash dry': 'mosás és szárítás',
            'wool': 'gyapjú',
        },
        'washer.drying_level': {
            'moist': 'nedves',
            'normal': 'normál',
            'extra': 'extra',
            'none': 'egyik sem',
        },

        'water_heater': {
            'water heater': 'vízforraló',
        },
    },
    
    'de': {
        'off': 'aus',
        'idle': 'Inaktiv',
        'busy': 'Beschäftigt',
        'pause': 'Pausiert',
        'fault': 'Fehler',

        '_globals': {
            'mode': 'Modus',
            'switch status': 'Schaltzustand',
            'battery level': 'Batterie-Ladestand',
            'target temperature': 'Zieltemperatur',
            'temperature': 'Temperatur',
            'relative humidity': 'Rel. Luftfeuchtigkeit',
            'illumination': 'Ausleuchtung',
            'indicator light': 'Kontrollleuchte',
            'physical control locked': 'Eingabe am Gerät blockiert',
        },

        'fan_level': {
            'auto': 'auto',
            # 'low': 'niedrig',
            # 'medium': 'medium',
            # 'middle': 'medium',
            # 'high': 'hoch',
            'quiet': 'ruhig',
            'turbo': 'turbo',
            'level1': 'Level 1',
            'level2': 'Level 2',
            'level3': 'Level 3',
            'level4': 'Level 4',
            'level5': 'Level 5',
            'level6': 'Level 6',
            'level7': 'Level 7',
        },

        'mode': {
            'auto': 'auto',
            'basic': 'basic',
            'low': 'niedrig',
            'medium': 'medium',
            'high': 'hoch',
            'sleep': 'schlafen',
            'smart': 'smart',
            'favorite': 'favorit',
        },

        'air_conditioner': {
            'air conditioner': 'Klimaanlage',
        },

        'air_conditioner.mode': {
            'cool': 'kühlen',
            'dry': 'trocknen',
            'fan': 'lüften',
            'heat': 'heizen',
        },

        'air_fresh.mode': {
            'auto': 'auto',
            'interval': 'intervall',
            'smart': 'smart',
            'silent': 'leise',
            'strong': 'stark',
            'none': 'keiner',
            'sleep': 'schlafen',
            'favorite': 'favorit',
        },

        'battery': {
            'battery battery level': 'Batterie-Level',
            'battery charging state': 'Ladezustand des Akkus',
        },

        'door_state': {
            'open': 'offen',
            'close': 'geschlossen',
            'close_timeout': 'nicht geschlossen timeout',
            'knock': 'klopfen',
            'breaking': 'zerstört',
            'stuck': 'tür klemmt',
        },

        'fan.mode': {
            'basic': 'basic',
            'basic wind': 'basic wind',
            'straight wind': 'starker Wind',
            'natural wind': 'natürlicher Wind',
            'energy saving': 'energie sparen',
            'none': 'nichts',
            'baby': 'baby',
            'smart': 'smart',
            'sleep': 'schlafen',
            'strong': 'stark',
            'circular wind': 'kreisförmiger Wind',
        },

        'ir_aircondition_control': {
            'ir aircondition control': 'Infrarot-Klimasteuerung',
            'mode for ir': 'infrarotmodus',
            'temperature for ir': 'infrarottemperatur',
            'turn on': 'einschalten',
            'turn off': 'ausschalten',
            'fan speed down': 'geschwindigkeit verringern',
            'fan speed up': 'geschwindigkeit erhöhen',
            'temperature down': 'kälter',
            'temperature up': 'wärmer',
        },
        'ir_aircondition_control.ir_mode': {
            'auto': 'auto',
            'cool': 'kühlen',
            'dry': 'trocken',
            'fan': 'lüften',
            'heat': 'heizen',
        },

        'light': {
            'light': '灯光',
        },
        'light.mode': {
            'day': 'Tag',
            'night': 'Nacht',
            'color': 'Farbe',
            'warmth': 'Sättigung',
            'tv': 'TV-Modus',
            'reading': 'Lesemodus',
            'computer': 'Computermodus',
            'hospitality': 'Besuchermodus',
            'entertainment': 'Unterhaltungsmodus',
            'lighting': 'Beleuchtung',
            'night light': 'Nachtlicht',
        },

        'lock_method': {
            'bluetooth': 'bluetooth',
            'password': 'passwort',
            'biological': 'biologisch',
            'key': 'schlüssel',
            'turntable': 'drehscheibe',
            'nfc': 'nfc',
            'one-time password': 'Einmal-Passwort',
            'two-step verification': 'Zwei-Faktor-Authentifizierung',
            'coercion': 'erzwungen',
            'homekit': 'homekit',
            'manual': 'manuell',
            'automatic': 'automatisch',
        },
        'lock_action': {
            'outside_unlock': 'von aussen entriegeln',
            'lock': 'gesperrt',
            'anti_lock_on': 'anti-lock ein',
            'anti_lock_off': 'anti-lock aus',
            'inside_unlock': 'von innen entriegeln',
            'lock_inside': 'von innen verschliessen',
            'child_lock_on': 'kindersicherung einschalten',
            'child_lock_off': 'kindersicherung ausschalten',
            'lock_outside': 'von aussen verschliessen',
        },

        'magnet_sensor': {
            'magnet sensor': 'tür- und fensterkontakt',
        },

        'motion_sensor': {
            'motion sensor': 'Bewegungserkennung',
            'motion sensor illumination': 'Lichtintensität',
        },

        'physical_control_locked': {
            'physical control locked': 'physikalische Pperre',
        },

        'play_control': {
            'play control': 'Wiedergabesteuerung',
            'keycodes': 'Tastencodes',
        },

        'power_consumption': {
            'power consumption': 'verbrauchte Energie',
            'power consumption electric power': 'Leistung',
            'power consumption electric current': 'elektrischer Strom',
            'power consumption electric voltage': 'Stromspannung',
        },

        'ptc_bath_heater': {
            'ptc bath heater': 'PTC Badheizung',
        },
        'ptc_bath_heater.mode': {
            'fan': 'Lüfter',
            'heat': 'Heizung',
            'ventilate': 'Belüften',
            'dry': 'entfeuchten',
            'defog': 'entnebeln',
            'quick heat': 'schnell heizen',
            'quick defog': 'schnelle entnebelung',
        },

        'speaker': {
            'speaker': 'Lautsprecher',
            'speaker volume': 'Lautstärke',
        },

        'sweep.suction_state': {
            'medium': 'medium',
            'silent': 'ruhig',
            'slient': 'ruhig',
            'standard': 'standard',
            'turbo': 'turbo',
        },

        'television': {
            'input control': 'eingangsquelle',
            'tv input control': 'tv-eingangsquelle',
        },

        'temperature_humidity_sensor': {
            'temperature humidity sensor temperature': 'temperatur',
            'temperature humidity sensor relative humidity': 'rel. luftfeuchtigkeit',
            'temperature humidity sensor atmospheric pressure': 'luftdruck',
        },

        'vacuum': {
            'robot cleaner': 'staubsaugerroboter',
            'robot cleaner status': 'staubsauger-status',
        },

        'vacuum.mode': {
            'basic': 'basic',
            'silent': 'ruhig',
            'standard': 'standard',
            'strong': 'stark',
            'turbo': 'turbo',
            'full speed': 'maximal',
        },

        'washer': {
            'drying level': 'Trocknungsgrad',
            'rinsh times': 'Anzahl Spülungen',
            'spin speed': 'Umdrehungsgeschwindigkeit',
            'target water level': 'Angestrebter Wasserstand',
        },
        'washer.mode': {
            'baby care': 'babywäsche',
            'boiling': 'kochwäsche',
            'color protection': 'farbschutzwäsche',
            'cotton': 'baumwolle',
            'daily wash': 'tägliche wäsche',
            'delicate wash': 'schonwäsche',
            'down coat': 'daunenjacke',
            'drum clean': 'trommelreinigung',
            'drum dry': 'trommel trocknen',
            'dry air wash': 'waschen mit trockener luft',
            'dry timing': 'trocknen zeitgesteuert',
            'dry': 'trocknen',
            'gold wash': 'gold wash',
            'heavy wash': 'schwere wäsche',
            'intensive': 'intensiv',
            'jacket': 'jacke',
            'jeans': 'jeans',
            'mite removal': 'milben entfernen',
            'quick wash dry': 'schnell waschen + trocknen',
            'quick wash': 'schnellwäsche',
            'rinse spin': 'spülmodus',
            'rinse': 'spülen',
            'shirt': 'shirt',
            'silk': 'seide',
            'soak wash': 'einweichen',
            'sock': 'socken',
            'spin': 'auswringen',
            'sportswear': 'sportkleidung',
            'super quick': 'super schnell',
            'synthetic': 'synthetik',
            'towel': 'handtücher',
            'underwear': 'unterwäsche',
            'user define': 'benutzerdefiniert',
            'wash dry': 'waschen + trocknen',
            'wool': 'wolle',
        },
        'washer.drying_level': {
            'moist': 'feucht',
            'normal': 'normal',
            'extra': 'extra',
            'none': 'keins',
        },

        'water_heater': {
            'water heater': 'Wasserkocher',
        },
    },
}
