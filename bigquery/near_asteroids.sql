CREATE TABLE `{project-id}.asteroids.near_asteroids` (
  id STRING NOT NULL,
  name STRING NOT NULL,
  magnitude STRING NOT NULL,
  min_diameter_estimated FLOAT64 NOT NULL,
  max_diameter_estimated FLOAT64 NOT NULL,
  is_hazardous BOOL NOT NULL
);
