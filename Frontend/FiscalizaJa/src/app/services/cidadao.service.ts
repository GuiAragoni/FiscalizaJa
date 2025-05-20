import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Cidadao {
  IdCidadao?: number;
  Nome: string;
  Email: string;
  Telefone: string;
  CPF: string;
  Endereco: string;
}

@Injectable({ providedIn: 'root' })
export class CidadaoService {
  private base = 'http://localhost:5000/cidadao';

  constructor(private http: HttpClient) {}

  listar(): Observable<Cidadao[]> {
    return this.http.get<Cidadao[]>(`${this.base}`);
  }

  obter(id: number): Observable<Cidadao> {
    return this.http.get<Cidadao>(`${this.base}/${id}`);
  }

  criar(dados: Cidadao): Observable<any> {
    return this.http.post(this.base, dados);
  }

  atualizar(id: number, dados: Cidadao): Observable<any> {
    return this.http.put(`${this.base}/${id}`, dados);
  }

  deletar(id: number): Observable<any> {
    return this.http.delete(`${this.base}/${id}`);
  }
}
