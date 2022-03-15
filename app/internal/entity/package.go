package entity

import "time"

type Package struct {
	Sku          string    `json:"sku"`
	Client       Client    `json:"client"`
	ShippingDate time.Time `json:"shipping_date"`
	DeliveryDate time.Time `json:"delivery_date"`
}
