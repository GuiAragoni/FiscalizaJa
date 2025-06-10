import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DescricaoOcorrenciaComponent } from './descricao-ocorrencia.component';

describe('DescricaoOcorrenciaComponent', () => {
  let component: DescricaoOcorrenciaComponent;
  let fixture: ComponentFixture<DescricaoOcorrenciaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DescricaoOcorrenciaComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DescricaoOcorrenciaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
