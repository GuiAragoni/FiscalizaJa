import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SecretariaHomeComponent } from './secretaria-home.component';

describe('SecretariaHomeComponent', () => {
  let component: SecretariaHomeComponent;
  let fixture: ComponentFixture<SecretariaHomeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SecretariaHomeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SecretariaHomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
