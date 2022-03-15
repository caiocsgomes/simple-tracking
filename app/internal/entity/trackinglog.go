package entity

type TrackingLog struct {
	Package Package `json:"package"`
	Address Address `json:"address"`
}
