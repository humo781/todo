from django.shortcuts import HttpResponse

def task_list(request):
    response = """
    <title>Vazifalar royhati</title>
    <h1>Yangi vazifa qoshish </h1>
    <p>Vazifa nomi: <input></p>
    <p>Tavsif: <textarea></textarea></p>
    <p>Muhimlik darajasi:<select>
    <option>past</option>
    <option>orta</option>
    <option>yuqori</option>
    </select> </p>
    <p>Muddat: <input type='date'></p>
    <button type='submit'>Vazifani qoshish</button>
    <h2>Mavjud Vazifalar</h2>   
    <table>
        <tr>
        <th>Vazifa</th>
        <th>Tavsif</th>
        <th>Muhimlik</th>
        <th>Muddat</th>
        <th>Holat</th>
        </tr>
        <tr>
        <td>Hisobot tayyorlash</td>
        <td>Moliyaviy hisobot</td>
        <td>Yuqori</td>
        <td>2024.27.11</td>
        <td>Bajarilmoqda</td>
        </tr>
        <tr>
        <td>Mijoz bilan uchrashuv</td>
        <td>Muzokaralar otkazish</td>
        <td>orta</td>
        <td>2024.27.11</td>
        <td>Rejalashtirilgan</td>
        </tr>
        <tr>
        <td>Slayd tayyorlash</td>
        <td>Taqdimot otkazish</td>
        <td>past</td>
        <td>2024.27.11</td>
        <td>Boshlanmagan</td>
    </table>    
    """
    return HttpResponse(response)



