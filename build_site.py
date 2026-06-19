import json
import os

# 1. Đọc dữ liệu từ file JSON do Gemini sinh ra
try:
    with open('exercises.json', 'r', encoding='utf-8') as f:
        exercises = json.load(f)
except FileNotFoundError:
    # Dữ liệu mẫu nếu chưa có file json
    exercises = [
        {"id": 1, "title": "Hàng phím cơ sở - Cơ bản", "description": "Luyện tập các phím ASDF JKL;", "level": "Cơ bản", "content": "asdf jkl; asdf jkl; aassddff jjkkll;;", "icon": "fa-keyboard"},
        {"id": 2, "title": "Mở rộng hàng phím trên", "description": "Luyện tập thêm các phím QWER UIOP", "level": "Cơ bản", "content": "aqsw defr jiko lupt qwer uiop", "icon": "fa-arrow-up-z-a"},
        # ... 50 bài tập sẽ nằm ở đây
    ]

# 2. Định nghĩa cấu trúc HTML mã nguồn
html_template = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ứng Dụng Luyện Gõ Bàn Phím QWERTY</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .correct { color: #10B981; }
        .incorrect { color: #EF4444; background-color: #FEE2E2; }
        .current { border-bottom: 2px solid #3B82F6; animation: blink 1s infinite; }
        @keyframes blink { 50% { border-color: transparent; } }
    </style>
</head>
<body class="bg-gray-50 font-sans min-h-screen">

    <header class="bg-blue-600 text-white shadow-md py-6 px-4 text-center">
        <h1 class="text-3xl font-bold"><i class="fa-solid fa-keyboard mr-2"></i>QWERTY Master</h1>
        <p class="text-blue-100 mt-2">Lộ trình 50 bài tập từ cơ bản đến nâng cao</p>
    </header>

    <main id="home-page" class="max-w-6xl mx-auto px-4 py-8">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="exercise-grid">
            </div>
    </main>

    <main id="practice-page" class="max-w-4xl mx-auto px-4 py-8 hidden">
        <button onclick="showHomePage()" class="mb-6 px-4 py-2 bg-gray-200 hover:bg-gray-300 text-gray-700 rounded-lg transition font-medium">
            <i class="fa-solid fa-arrow-left mr-2"></i> Quay lại trang chủ
        </button>
        
        <div class="bg-white rounded-xl shadow-lg p-6 md:p-8">
            <div class="flex justify-between items-center mb-6">
                <h2 id="practice-title" class="text-2xl font-bold text-gray-800">Tên bài tập</h2>
                <span id="practice-level" class="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm font-semibold">Cơ bản</span>
            </div>
            <p id="practice-desc" class="text-gray-600 mb-6 italic">Mô tả bài tập</p>

            <div id="text-display" class="bg-gray-100 p-6 rounded-lg text-xl tracking-wide font-mono mb-6 select-none leading-relaxed min-h-[100px]"></div>

            <input type="text" id="keyboard-input" class="absolute opacity-0 w-0 h-0" autofocus>
            
            <div class="text-center">
                <p class="text-sm text-gray-400 animate-pulse">Nhấp vào vùng chữ và bắt đầu gõ để luyện tập...</p>
            </div>

            <div class="grid grid-cols-3 gap-4 mt-8 pt-6 border-t border-gray-100 text-center">
                <div><p class="text-gray-500 text-sm">Tiến độ</p><p id="stat-progress" class="text-xl font-bold text-gray-800">0%</p></div>
                <div><p class="text-gray-500 text-sm">Sai sót</p><p id="stat-errors" class="text-xl font-bold text-red-500">0</p></div>
                <div><p class="text-gray-500 text-sm">Kết quả</p><p id="stat-status" class="text-xl font-bold text-gray-400">Chưa xong</p></div>
            </div>
        </div>
    </main>

    <script>
        const exercises = {exercises_json};
        let currentExercise = null;
        let typedIndex = 0;
        let errorCount = 0;

        // Hiển thị danh sách bài tập lên Grid
        function renderGrid() {
            const grid = document.getElementById('exercise-grid');
            grid.innerHTML = exercises.map(ex => `
                <div class="bg-white rounded-xl shadow-sm hover:shadow-md transition duration-300 p-6 border border-gray-100 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center space-x-4 mb-4">
                            <div class="w-12 h-12 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center text-2xl">
                                <i class="fa-solid ${ex.icon || 'fa-keyboard'}"></i>
                            </div>
                            <div>
                                <span class="text-xs font-semibold px-2 py-0.5 rounded bg-gray-100 text-gray-600">${ex.level}</span>
                                <h3 class="font-bold text-gray-800 mt-1">${ex.title}</h3>
                            </div>
                        </div>
                        <p class="text-gray-600 text-sm line-clamp-2">${ex.description}</p>
                    </div>
                    <button onclick="startExercise(${ex.id})" class="mt-6 w-full py-2 bg-blue-50 hover:bg-blue-600 text-blue-600 hover:text-white rounded-lg transition font-medium text-sm text-center">
                        Luyện tập <i class="fa-solid fa-chevron-right ml-1 text-xs"></i>
                    </button>
                </div>
            `).join('');
        }

        function startExercise(id) {
            currentExercise = exercises.find(e => e.id === id);
            typedIndex = 0;
            errorCount = 0;
            
            document.getElementById('home-page').classList.add('hidden');
            document.getElementById('practice-page').classList.remove('hidden');
            
            document.getElementById('practice-title').innerText = currentExercise.title;
            document.getElementById('practice-desc').innerText = currentExercise.description;
            document.getElementById('practice-level').innerText = currentExercise.level;
            
            renderTextDisplay();
            
            const input = document.getElementById('keyboard-input');
            input.value = '';
            input.focus();
            
            // Lắng nghe sự kiện click vào khung để focus lại input
            document.getElementById('text-display').onclick = () => input.focus();
        }

        function showHomePage() {
            document.getElementById('home-page').classList.remove('hidden');
            document.getElementById('practice-page').classList.add('hidden');
        }

        function renderTextDisplay() {
            const container = document.getElementById('text-display');
            const content = currentExercise.content;
            
            container.innerHTML = content.split('').map((char, index) => {
                let className = '';
                if (index < typedIndex) className = 'correct';
                else if (index === typedIndex) className = 'current';
                return `<span class="${className}">${char}</span>`;
            }).join('');
        }

        // Xử lý sự kiện gõ phím
        document.getElementById('keyboard-input').addEventListener('input', (e) => {
            const content = currentExercise.content;
            const inputVal = e.target.value;
            const lastChar = inputVal[inputVal.length - 1];

            if (typedIndex < content.length) {
                if (lastChar === content[typedIndex]) {
                    typedIndex++;
                } else {
                    errorCount++;
                    // Hiệu ứng nhấp nháy đỏ khi gõ sai
                    const currentSpan = document.querySelector('.current');
                    if (currentSpan) {
                        currentSpan.classList.add('incorrect');
                        setTimeout(() => currentSpan.classList.remove('incorrect'), 200);
                    }
                }
                
                // Cập nhật thông tin thống kê
                document.getElementById('stat-progress').innerText = Math.round((typedIndex / content.length) * 100) + '%';
                document.getElementById('stat-errors').innerText = errorCount;
                
                renderTextDisplay();
                
                if (typedIndex === content.length) {
                    document.getElementById('stat-status').innerText = 'Hoàn thành 🎉';
                    document.getElementById('stat-status').className = 'text-xl font-bold text-emerald-500';
                }
            }
        });

        // Khởi chạy ban đầu
        renderGrid();
    </script>
</body>
</html>
"""

# Chèn dữ liệu JSON vào mã nguồn HTML
final_html = html_template.replace("{exercises_json}", json.dumps(exercises, ensure_ascii=False))

# Xuất ra file index.html
os.makedirs('dist', exist_ok=True)
with open('dist/index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Đã biên dịch thành công! File web tĩnh nằm tại: dist/index.html")