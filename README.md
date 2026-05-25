# bareos-hyperv-plugin

GitHub Actions build pipeline for `hyper-v-fd.dll` — el plugin de Bareos para backup de VMs Hyper-V.

## Como usar

1. Ir a **Actions** → **Build hyper-v-fd.dll** → **Run workflow**
2. Esperar ~30-45 min (primera vez, vcpkg sin cache)
3. Descargar el artifact `hyper-v-fd-<N>.zip` con el `.dll`
4. Instalar `bareos-fd` en el Hyper-V host y copiar el `.dll` a `C:\Program Files\Bareos\Plugins\`

## Fuente

Compilado desde [bareos/bareos](https://github.com/bareos/bareos) master — `core/src/win32/plugins/filed/hyper-v.cc`

Licencia: AGPLv3
