import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AirQualityDetailComponent } from './components/air-quality-detail/air-quality-detail.component';
import { AirQualityForecastComponent } from './components/air-quality-forecast/air-quality-forecast.component';

@NgModule({
  declarations: [
    AppComponent,
    AirQualityDetailComponent,
    AirQualityForecastComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
