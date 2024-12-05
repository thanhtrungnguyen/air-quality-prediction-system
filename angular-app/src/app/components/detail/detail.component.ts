import { Component, Input, OnChanges } from '@angular/core';
import { AirQualityService } from '../../services/air-quality.service';

@Component({
  selector: 'app-detail',
  standalone: true,
  imports: [],
  templateUrl: './detail.component.html',
  styleUrl: './detail.component.css'
})
export class DetailComponent implements OnChanges {
  @Input() selectedDate: string = '';
  airQualityDetails: any;

  constructor(private airQualityService: AirQualityService) { }

  ngOnChanges(): void {
    if (this.selectedDate) {
      this.airQualityService.getAirQualityData().subscribe((data) => {
        this.airQualityDetails = data.find(
          (record) => record.date === this.selectedDate
        );
      });
    }
  }
}
