CREATE TABLE "client" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "email" timestamp,
  "address_id" int,
  "company_id" int
);

CREATE TABLE "address" (
  "id" int PRIMARY KEY,
  "street" varchar,
  "number" int,
  "postal_code" varchar,
  "city" varchar,
  "state" varchar,
  "address_type" varchar,
  "preferred" boolean
);

CREATE TABLE "company" (
  "id" int PRIMARY KEY,
  "name" varchar,
  "address_id" int
);

CREATE TABLE "package" (
  "id" int PRIMARY KEY,
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

ALTER TABLE "client" ADD FOREIGN KEY ("company_id") REFERENCES "company" ("id");

ALTER TABLE "address" ADD FOREIGN KEY ("id") REFERENCES "client" ("address_id");

ALTER TABLE "address" ADD FOREIGN KEY ("id") REFERENCES "company" ("address_id");

ALTER TABLE "package" ADD FOREIGN KEY ("client_id") REFERENCES "client" ("id");

ALTER TABLE "tracking_log" ADD FOREIGN KEY ("package_id") REFERENCES "package" ("id");