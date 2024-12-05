import { Component, OnInit } from '@angular/core';
import { AirQualityService } from '../../services/air-quality.service';

@Component({
  selector: 'app-timeline',
  standalone: true,
  imports: [],
  templateUrl: './timeline.component.html',
  styleUrl: './timeline.component.css'
})
export class TimelineComponent implements OnInit {
  airQualityData: any[] = [];
  selectedDate: string = '';

  constructor(private airQualityService: AirQualityService) { }

  ngOnInit(): void {
    this.airQualityService.getAirQualityData().subscribe((data) => {
      this.airQualityData = data;
    });
  }

  selectDate(date: string): void {
    this.selectedDate = date;
    // Emit event to update details component (if necessary)
  }
}
