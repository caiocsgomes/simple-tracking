package entity

type AddressType int

const (
	CompanyAddress AddressType = iota
	ClientAddress
	DepositAddress
)

type Address struct {
	Street      string      `json:"street"`
	Number      int         `json:"number"`
	PostalCode  string      `json:"postal_code"`
	City        string      `json:"city"`
	State       string      `json:"state"`
	AddressType AddressType `json:"address_type"`
}
