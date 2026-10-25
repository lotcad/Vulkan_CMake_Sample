// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    public static partial class CadApi
    {
        public const int CAD_PARTICLE_FIRE = 0;
        public const int CAD_PARTICLE_SMOKE = 1;
        public const int CAD_PARTICLE_SPARKS = 2;
        public const int CAD_PARTICLE_PAUSE = 0;
        public const int CAD_PARTICLE_PLAY = 1;
        public const int CAD_PARTICLE_RESET = 2;

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateParticleEmitter(int preset, CAD_GeVec3 position, double unitsPerMeter, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateParticleEmitter — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateParticleEmitter(int preset, CAD_GeVec3 position, double unitsPerMeter, out uint outId)
        {
            return CAD_CreateParticleEmitter(preset, position, unitsPerMeter, null, out outId);
        }
        /// <summary>CAD_CreateParticleEmitter — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateParticleEmitter(int preset, CAD_GeVec3 position, double unitsPerMeter, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateParticleEmitter(preset, position, unitsPerMeter, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateParticleEmitterFromPreset([MarshalAs(UnmanagedType.LPUTF8Str)] string path, CAD_GeVec3 position, double unitsPerMeter, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateParticleEmitterFromPreset — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateParticleEmitterFromPreset(string path, CAD_GeVec3 position, double unitsPerMeter, out uint outId)
        {
            return CAD_CreateParticleEmitterFromPreset(path, position, unitsPerMeter, null, out outId);
        }
        /// <summary>CAD_CreateParticleEmitterFromPreset — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateParticleEmitterFromPreset(string path, CAD_GeVec3 position, double unitsPerMeter, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateParticleEmitterFromPreset(path, position, unitsPerMeter, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateExternalEffect([MarshalAs(UnmanagedType.LPUTF8Str)] string path, CAD_GeVec3 position, double unitsPerMeter, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateExternalEffect — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateExternalEffect(string path, CAD_GeVec3 position, double unitsPerMeter, out uint outId)
        {
            return CAD_CreateExternalEffect(path, position, unitsPerMeter, null, out outId);
        }
        /// <summary>CAD_CreateExternalEffect — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateExternalEffect(string path, CAD_GeVec3 position, double unitsPerMeter, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateExternalEffect(path, position, unitsPerMeter, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetParticlePlayback(uint id, int state);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetParticleSettingsJson(uint id, byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetParticleSettingsJson(uint id, [MarshalAs(UnmanagedType.LPUTF8Str)] string json);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetParticleLiveCount(uint id);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetParticlePresetCount();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetParticlePresetName(int index, byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetParticlePresetPath(int index, byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SaveParticlePreset(uint id, [MarshalAs(UnmanagedType.LPUTF8Str)] string path);
    }
}
