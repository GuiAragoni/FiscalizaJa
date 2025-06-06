import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class CidadaoService { 

  apiUrl = 'http://127.0.0.1:5000/';

  constructor(private http: HttpClient) { }

  registrarCidadao(dados: any): Observable<any> {      
    return this.http.post(this.apiUrl + "registrar", dados);
  }

  loginCidadao(dados: any): Observable<any> {   
    debugger   
    return this.http.get(`${this.apiUrl}cidadao/${dados}`);
  }
}

