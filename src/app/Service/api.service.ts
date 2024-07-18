import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private baseUrl = 'http://127.0.0.1:5000/ask';

  constructor(private http: HttpClient) {}

  sendUserMessage(question: string): Observable<any> {
    const session_id = this.getCookie('session_id');

    return this.http.post<any>(this.baseUrl, { question, session_id });
  
  }

  private getCookie(name: string): string {
    const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : '';
  }
}
