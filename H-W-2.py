import time
arabic = ['ا','ب','ت','ث','ج','ح','خ','د','ذ','ر','ز','س','ش','ص','ض',
          'ط','ظ','ع','غ','ف','ق','ك','ل','م','ن','ه','و','ي']

def caesar(text, shift, language='arabic', mode='encrypt'):
    output = ""
    for ch in text:
        if language == 'arabic' and ch in arabic:
            i = arabic.index(ch)
            if mode == 'encrypt':
                new_i = (i + shift) % len(arabic)
            else:
                new_i = (i - shift) % len(arabic)
            output += arabic[new_i]
        elif language == 'english' and ch.isalpha():
            if ch.islower():
                i = ord(ch) - ord('a')
                if mode == 'encrypt':
                    output += chr((i + shift) % 26 + ord('a'))
                else:
                    output += chr((i - shift) % 26 + ord('a'))
            else:
                i = ord(ch) - ord('A')
                if mode == 'encrypt':
                    output += chr((i + shift) % 26 + ord('A'))
                else:
                    output += chr((i - shift) % 26 + ord('A'))
        else:
            output += ch
    return output

# اختيار اللغة
lang = input(" هل النص عربي (ar) : or  انكليزي(en) ؟ ").strip().lower()

# اختيار العملية
action = input("هل تريد تشفير (1) أم فك التشفير (2)؟ ").strip()

# إدخال النص
text = input("أدخل النص: ")

start = time.time()

if action == "1":
   
    key = int(input("اختر مفتاح التشفير (رقم): "))
    result = caesar(text, key, language=lang, mode='encrypt')
    print("النص المشفر:", result)

elif action == "2":
   
    print("\n=== جميع احتمالات فك التشفير ===")
    if lang == 'ar':
        for key in range(1, len(arabic)):
            print(f"[مفتاح {key}] -> {caesar(text, key, language='arabic', mode='decrypt')}")
    elif lang == 'en':
        for key in range(1, 26):
            print(f"[Key {key}] -> {caesar(text, key, language='english', mode='decrypt')}")
    else:
        print("لغة غير صحيحة!")
else:
    print("خيار غير صحيح!")

end = time.time()
print("الوقت المستغرق: {:.4f} ثانية".format(end - start))