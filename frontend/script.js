// 原index中的<script></script>标签内内容搬到这里
// <script>这个标签本身不搬运
function changeText() {
    document.getElementById('msg').textContent = '你刚刚触发了一段 JavaScript。';
}