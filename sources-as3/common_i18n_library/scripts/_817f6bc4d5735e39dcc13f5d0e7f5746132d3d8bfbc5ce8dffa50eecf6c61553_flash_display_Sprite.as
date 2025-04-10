package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _817f6bc4d5735e39dcc13f5d0e7f5746132d3d8bfbc5ce8dffa50eecf6c61553_flash_display_Sprite extends Sprite
   {
       
      
      public function _817f6bc4d5735e39dcc13f5d0e7f5746132d3d8bfbc5ce8dffa50eecf6c61553_flash_display_Sprite()
      {
         super();
      }
      
      public function allowDomainInRSL(... rest) : void
      {
         Security.allowDomain.apply(null,rest);
      }
      
      public function allowInsecureDomainInRSL(... rest) : void
      {
         Security.allowInsecureDomain.apply(null,rest);
      }
   }
}
