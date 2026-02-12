package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _126ecf8716e2b5d59dd66da96f6a878d4f147b597da77a5b1180b235ba836f9e_flash_display_Sprite extends Sprite
   {
       
      
      public function _126ecf8716e2b5d59dd66da96f6a878d4f147b597da77a5b1180b235ba836f9e_flash_display_Sprite()
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
