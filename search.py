import json
import os


def search_korean_phrase(kr, data):
    '''
    Enter a Korean phrase to search in data
    '''
    results = []
    for entry in data:
        if entry.get('kr') and kr in entry['kr']:
            results.append(entry)
    return results

def add_translation(kr, eng, data, file_path):
    '''
    Add new entry to data
    '''
    data.append({'kr': kr, 'eng': eng})

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    file_path = 'data.json'

    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    while True:
        print("1. Search KR phrase")
        print("2. Add new word")
        print("3. Exit")

        choice = input().strip()

        if choice == '1':
            while True:
                kr = input("Korean to search: ").strip()
                if kr.lower() == 'back':
                    break
                results = search_korean_phrase(kr, data)
                if results:
                    for result in results:
                        print(f"\nKR: {result['kr']}\nENG: {result['eng']}\n")
                else:
                    print("No match found")
            
        elif choice == '2':
            while True:
                kr = input("KR: ").strip()
                if kr.lower() == 'back':
                    break
                eng = input("ENG: ").strip()
                add_translation(kr, eng, data, file_path)
                print(f"{kr} -> {eng}")

        elif choice == '3':
            break

    
   

if __name__ == "__main__":
    main()