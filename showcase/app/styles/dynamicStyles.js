import Airflow from "../../public/icons/airflow.svg";
import Automation from "../../public/icons/automation.svg";
import BigQuery from "../../public/icons/bigquery.svg";
import Dagster from "../../public/icons/dagster.svg";
import DBT from "../../public/icons/dbt.svg";
import Docker from "../../public/icons/docker.svg";
import Fabric from "../../public/icons/fabric.svg";
import GoogleLooker from "../../public/icons/lookerstudio.svg";
import MachineLearning from "../../public/icons/machinelearning.svg";
import Metabase from "../../public/icons/metabase.svg";
import PostgreSQL from "../../public/icons/postgresql.svg";
import PowerBI from "../../public/icons/powerbi.svg";
import Python from "../../public/icons/python.svg";
import Snowflake from "../../public/icons/snowflake.svg";

const styles = {
  'toolLabel': {
    'Airflow': <Airflow />,
    'Automation': <Automation />,
    'BigQuery': <BigQuery />,
    'Dagster': <Dagster />,
    'dbt': <DBT />,
    'Docker': <Docker />,
    'Fabric': <Fabric />,
    'Google Looker': <GoogleLooker />,
    'Machine Learning': <MachineLearning />,
    'Metabase': <Metabase />,
    'PostgreSQL': <PostgreSQL />,
    'Power BI': <PowerBI />,
    'Python': <Python />,
    'Snowflake': <Snowflake />,
  },
  'outline': {
    'Airflow': 'shadow-greenAirflow',
    'Automation': 'shadow-redAutomation',
    'BigQuery': 'shadow-blueBigQuery',
    'Dagster': 'shadow-purpleDagster',
    'dbt': 'shadow-orangedbt',
    'Docker': 'shadow-blueDocker',
    'Fabric': 'shadow-greenFabric',
    'Google Looker': 'shadow-greenGoogleLooker',
    'Machine Learning': 'shadow-purpleMachineLearning',
    'Metabase': 'shadow-blueMetabase',
    'PostgreSQL': 'shadow-bluePostgreSQL',
    'Power BI': 'shadow-yellowPowerBI',
    'Python': 'shadow-bluePython',
    'Snowflake': 'shadow-blueSnowflake',
  },
  'hover': {
    'Airflow': 'hover:text-greenAirflow',
    'Automation': 'hover:text-redAutomation',
    'BigQuery': 'hover:text-blueBigQuery',
    'Dagster': 'hover:text-purpleDagster',
    'dbt': 'hover:text-orangedbt',
    'Docker': 'hover:text-blueDocker',
    'Fabric': 'hover:text-greenFabric',
    'Google Looker': 'hover:text-greenGoogleLooker',
    'Machine Learning': 'hover:text-purpleMachineLearning',
    'Metabase': 'hover:text-blueMetabase',
    'PostgreSQL': 'hover:text-bluePostgreSQL',
    'Power BI': 'hover:text-yellowPowerBI',
    'Python': 'hover:text-bluePython',
    'Snowflake': 'hover:text-blueSnowflake',
  },
  'label': {
    'Airflow': 'text-greenAirflow ring-greenAirflow',
    'Automation': 'text-redAutomation ring-redAutomation',
    'BigQuery': 'text-blueBigQuery ring-blueBigQuery',
    'Dagster': 'text-purpleDagster ring-purpleDagster',
    'dbt': 'text-orangedbt ring-orangedbt',
    'Docker': 'text-blueDocker ring-blueDocker',
    'Fabric': 'text-greenFabric ring-greenFabric',
    'Google Looker': 'text-greenGoogleLooker ring-greenGoogleLooker',
    'Machine Learning': 'text-purpleMachineLearning ring-purpleMachineLearning',
    'Metabase': 'text-blueMetabase ring-blueMetabase',
    'PostgreSQL': 'text-bluePostgreSQL ring-bluePostgreSQL',
    'Power BI': 'text-yellowPowerBI ring-yellowPowerBI',
    'Python': 'text-bluePython ring-bluePython',
    'Snowflake': 'text-blueSnowflake ring-blueSnowflake',
  }
}

export default styles;