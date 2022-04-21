CREATE TABLE "client" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "email" timestamp,
  "address_id" int
);

CREATE TABLE "address" (
  "id" SERIAL PRIMARY KEY,
  "street" varchar,
  "number" int,
  "postal_code" varchar,
  "city" varchar,
  "state" varchar,
  "address_type" varchar
);

CREATE TABLE "company" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "address_id" int
);

CREATE TABLE "package" (
  "id" SERIAL PRIMARY KEY,
  "sku" varchar,
  "client_id" int,
  "shipping_date" timestamp,
  "delivery_date" timestamp,
  "delivered" boolean
);

CREATE TABLE "tracking_log" (
  "package_id" int,
  "coord" point,
  "date" timestamp
);

ALTER TABLE "client" ADD FOREIGN KEY ("address_id") REFERENCES "address" ("id");

ALTER TABLE "company" ADD FOREIGN KEY ("address_id") REFERENCES "address" ("id");

ALTER TABLE "package" ADD FOREIGN KEY ("client_id") REFERENCES "client" ("id");

ALTER TABLE "tracking_log" ADD FOREIGN KEY ("package_id") REFERENCES "package" ("id");