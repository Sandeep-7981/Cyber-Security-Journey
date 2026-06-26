def get_styles():
    return """
<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    font-family:Segoe UI,Arial,sans-serif;
    background:#eef2f7;
    color:#1f2937;
    padding:40px;
}

.container{
    max-width:1300px;
    margin:auto;
    background:white;
    border-radius:15px;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
    overflow:hidden;
}

.header{
    background:linear-gradient(135deg,#1e3a8a,#2563eb);
    color:white;
    padding:40px;
    text-align:center;
}

.header h1{
    font-size:38px;
    margin-bottom:10px;
}

.header p{
    font-size:17px;
    opacity:.9;
}

.content{
    padding:35px;
}

h2{
    margin-top:35px;
    margin-bottom:15px;
    color:#1e3a8a;
    border-left:6px solid #2563eb;
    padding-left:10px;
}

.summary{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:20px;
    margin-top:25px;
}

.card{
    color:white;
    border-radius:12px;
    padding:25px;
    text-align:center;
    transition:.3s;
}

.card:hover{
    transform:translateY(-5px);
}

.card h3{
    font-size:18px;
    margin-bottom:10px;
}

.card p{
    font-size:34px;
    font-weight:bold;
}

.total{
    background:#2563eb;
}

.failed{
    background:#dc2626;
}

.success-card{
    background:#16a34a;
}

.unique{
    background:#7c3aed;
}

.ioc{
    background:#ea580c;
}

.high{
    background:#991b1b;
}

table{
    width:100%;
    border-collapse:collapse;
    margin-top:15px;
    margin-bottom:25px;
}

th{
    background:#2563eb;
    color:white;
    padding:14px;
    text-align:left;
}

td{
    padding:12px;
    border-bottom:1px solid #ddd;
}

tr:nth-child(even){
    background:#f9fafb;
}

tr:hover{
    background:#eef4ff;
}

.badge{
    color:white;
    padding:6px 14px;
    border-radius:25px;
    font-size:13px;
    font-weight:bold;
}

.success{
    background:#16a34a;
}

.danger{
    background:#dc2626;
}

.warning{
    background:#f59e0b;
}

.info{
    background:#2563eb;
}

.footer{
    margin-top:40px;
    background:#f3f4f6;
    padding:20px;
    text-align:center;
    color:#6b7280;
    border-top:1px solid #ddd;
}

hr{
    margin:25px 0;
    border:none;
    border-top:1px solid #ddd;
}

ul{
    padding-left:20px;
}

li{
    margin-bottom:10px;
}

.metadata{
    background:#f8fafc;
    border-left:5px solid #2563eb;
    padding:18px;
    border-radius:8px;
    margin-top:20px;
    line-height:1.8;
}

</style>
"""