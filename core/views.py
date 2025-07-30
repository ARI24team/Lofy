from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token
from django.urls import reverse

@login_required(login_url='accounts:login')
def homeview(request):
    logout_url = reverse('accounts:logout')
    csrf_token = get_token(request)

    html = f"""
        <h2>Welcome back, {request.user.username}!</h2>
        <form action="{logout_url}" method="POST" style="display:inline;">
            <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">"""
    if not request.user.email_confirmed: 
            html+="<p> Verify your email</p>"
            
    html+=f"""<button 
                type="submit" 
                style="
                    padding:8px 16px; 
                    background-color:#f44336; 
                    color:white; 
                    border:none; 
                    border-radius:4px; 
                    font-family:sans-serif; 
                    font-size:14px; 
                    cursor:pointer;"
                onmouseover="this.style.backgroundColor='#d32f2f'" 
                onmouseout="this.style.backgroundColor='#f44336'">
                Logout
            </button>
        </form>
    """
    return HttpResponse(html)
